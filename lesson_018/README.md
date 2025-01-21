## Lesson_018 task
Using the data presented in the form of three categories of animal images (chicken, sheep, squirrel) already previously divided into training and test sets (train and test folders), train a three-category classifier based on a convolutional neural network.
Notes:
1. Use the basic architecture of the neural network as in the example presented in the lesson.
2. Set class_mode='categorical' for the flow_from_directory method (in this case, these are train_data_augmented_shuffled and test_data generators).
3. When describing the architecture of the neural network in the output layer, provide not one, but three outputs, the activation function is softmax (Dense(3, activation="softmax")).
4. When compiling the model, select the loss-function categorical_crossentropy (loss="categorical_crossentropy").
5. Select the number of epochs (from 20 to 40) so that there is no stable effect of retraining the neural network.
6. Demonstrate the work of the trained three-category classifier on the example of 9 random images (3 for each of the categories) that did not participate in either the training or test samples.