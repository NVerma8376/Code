import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from PIL import Image

# Define the model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = x.view(-1, 28 * 28)  # Flatten the input
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Training function
def train_model():
    # Prepare the dataset
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

    # Initialize model, loss, and optimizer
    model = SimpleNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Train the model
    epochs = 5
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader):.4f}")

    # Save the model
    torch.save(model.state_dict(), 'simple_nn.pth')
    print("Model saved to 'simple_nn.pth'.")
    return model

# Prediction function
def predict_image(model, image_path):
    # Define transformations
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # Load and preprocess the image
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    input_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    # Make prediction
    model.eval()  # Set the model to evaluation mode
    with torch.no_grad():
        output = model(input_tensor)
        _, predicted_class = torch.max(output, 1)
    print(f"Predicted digit: {predicted_class.item()}")

# Main script
if __name__ == '__main__':
    import os
    
    # Train the model if it doesn't exist
    if not os.path.exists('simple_nn.pth'):
        print("Training the model...")
        model = train_model()
    else:
        print("Loading the existing model...")
        model = SimpleNN()
        model.load_state_dict(torch.load('simple_nn.pth'))
        model.eval()

    # Predict on a new image
    image_path = '/home/nverma/Documents/GitHub/Code/Pytorch/pixil-frame-0.png'  # Replace with the path to your image
    if os.path.exists(image_path):
        predict_image(model, image_path)
    else:
        print(f"Image file '{image_path}' not found. Please provide a valid path.")
