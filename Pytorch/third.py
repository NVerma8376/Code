import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.optimizers import Adam

class ZeroOnePredictor:
    def __init__(self):
        self.model = self.build_model()
        self.data = []
    
    def build_model(self):
        # Sequential model with LSTM to learn binary sequences
        model = Sequential([
            Embedding(input_dim=2, output_dim=8, input_length=5),  # Embedding layer for binary input
            LSTM(16, return_sequences=False),                     # LSTM layer to process sequences
            Dense(1, activation='sigmoid')                       # Output layer with sigmoid activation
        ])
        model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def add_data(self, sequence, label):
        """Add training data."""
        self.data.append((sequence, label))

    def train(self, epochs=10):
        """Train the model if there is enough data."""
        if len(self.data) < 10:  # Require at least 10 data points
            print("Not enough data to train the model yet.")
            return
        
        # Prepare the dataset
        sequences, labels = zip(*self.data)
        sequences = np.array(sequences)
        labels = np.array(labels)
        
        # Train the model
        self.model.fit(sequences, labels, epochs=epochs, verbose=0)
        print("Model trained!")

    def predict(self, sequence):
        """Predict the next number given a sequence."""
        sequence = np.array(sequence).reshape(1, -1)
        prediction = self.model.predict(sequence, verbose=0)[0][0]
        return 1 if prediction >= 0.5 else 0


def main():
    predictor = ZeroOnePredictor()

    print("Let's start! I'll try to predict whether you'll say 0 or 1.")
    print("Provide a sequence of 5 numbers (0 or 1). Press 'Ctrl+C' to exit.")

    try:
        while True:
            sequence = input("Enter a sequence of 5 numbers (e.g., '0 1 0 1 0'): ")
            sequence = list(map(int, sequence.split()))
            
            if len(sequence) != 5 or any(x not in [0, 1] for x in sequence):
                print("Invalid input. Please enter exactly 5 numbers (0 or 1).")
                continue
            
            prediction = predictor.predict(sequence)
            print(f"My guess for your next number is: {prediction}")
            
            actual = int(input("What was your actual number (0 or 1)? "))
            if actual not in [0, 1]:
                print("Invalid number. Please enter 0 or 1.")
                continue
            
            predictor.add_data(sequence, actual)
            predictor.train()

    except KeyboardInterrupt:
        print("\nExiting. Thanks for playing!")
        print("Goodbye!")


if __name__ == "__main__":
    main()
