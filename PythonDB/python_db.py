import os
import json
from typing import Any, Dict, List, Optional
import time

class SimpleDB:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.data_file = f"{db_name}.json"
        self.index = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load data from file if it exists"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.index = json.load(f)
            except json.JSONDecodeError:
                self.index = {}
        else:
            self.index = {}
    
    def _save_data(self) -> None:
        """Save data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.index, f, indent=2)
    
    def insert(self, key: str, value: Any) -> bool:
        """Insert a key-value pair into the database"""
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        self.index[key] = {
            'value': value,
            'timestamp': time.time()
        }
        self._save_data()
        return True
    
    def get(self, key: str) -> Optional[Any]:
        """Retrieve a value by key"""
        record = self.index.get(key)
        return record['value'] if record else None
    
    def update(self, key: str, value: Any) -> bool:
        """Update value for existing key"""
        if key not in self.index:
            return False
        
        self.index[key] = {
            'value': value,
            'timestamp': time.time()
        }
        self._save_data()
        return True
    
    def delete(self, key: str) -> bool:
        """Delete a key-value pair"""
        if key not in self.index:
            return False
        
        del self.index[key]
        self._save_data()
        return True
    
    def list_keys(self) -> List[str]:
        """List all keys in the database"""
        return list(self.index.keys())
    
    def clear(self) -> None:
        """Clear all data from database"""
        self.index = {}
        self._save_data()
    
    def get_size(self) -> int:
        """Get number of records in database"""
        return len(self.index)

# Example usage:
if __name__ == "__main__":
    # Create a new database
    db = SimpleDB("test_db")
    
    # Insert some data
    db.insert("user1", {"name": "John", "age": 30})
    db.insert("user2", {"name": "Alice", "age": 25})
    
    # Get data
    print("User1:", db.get("user1"))
    
    # Update data
    db.update("user1", {"name": "John", "age": 31})
    
    # List all keys
    print("All keys:", db.list_keys())
    
    # Get database size
    print("Database size:", db.get_size())