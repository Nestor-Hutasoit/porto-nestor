# Indonesian Hate Speech & Abusive Language Detection

A hybrid deep learning approach for classifying Indonesian tweets as hate speech or abusive language. This project explores the combination of traditional sequence models with attention mechanisms to capture both local n-gram patterns and global context within social media text.

## Tech Stack
* **Language:** Python
* **Frameworks:** TensorFlow/Keras, Scikit-Learn, Pandas
* **Architectures:** Multi-Scale CNN, Bidirectional LSTM, Transformer Encoder

## Key Features
* **Advanced Text Preprocessing:** Normalized Indonesian slang ("bahasa alay") to formal vocabulary and engineered an explicit manual feature that counts abusive words per tweet to provide a stronger signal to the model.
* **Hybrid Model Design:** Built and evaluated two sophisticated architectures: a Multi-Scale CNN + Transformer designed for local phrase detection, and a Bidirectional LSTM + Transformer optimized for long-term sequential dependencies.
* **Robust Validation Pipeline:** Implemented Stratified 5-Fold Cross-Validation to ensure model stability across different data splits and to mitigate high variance or overfitting.
* **Training Optimization:** Applied Early Stopping, ReduceLROnPlateau, and ModelCheckpoint callbacks during the training process to dynamically adjust learning rates and save the best model weights based on validation AUC.
* **High-Performance Classification:** The tuned LSTM + Transformer model successfully achieved an F1-Score of 0.87 and an AUC of 0.96 on the final test set, demonstrating highly accurate abusive language detection.
