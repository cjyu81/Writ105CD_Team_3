import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class QuestionnaireForm {
    public static void main(String[] args) {
        // Create the main frame
        JFrame frame = new JFrame("Questionnaire Form");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new GridLayout(6, 1));

        // Create components
        JLabel nameLabel = new JLabel("What is your name?");
        JTextField nameField = new JTextField();

        JLabel ageLabel = new JLabel("How old are you?");
        JTextField ageField = new JTextField();

        JLabel colorLabel = new JLabel("Would you like the ADHD filter?");
        JTextField colorField = new JTextField();

        JButton submitButton = new JButton("Submit");
        JTextArea resultArea = new JTextArea();
        resultArea.setEditable(false);

        // Add components to the frame
        frame.add(nameLabel);
        frame.add(nameField);
        frame.add(ageLabel);
        frame.add(ageField);
        frame.add(colorLabel);
        frame.add(colorField);
        frame.add(submitButton);
        frame.add(new JScrollPane(resultArea));

        // Add button action listener
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = nameField.getText();
                String age = ageField.getText();
                String color = colorField.getText();

                if (name.isEmpty() || age.isEmpty() || color.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Please fill in all fields!", "Error", JOptionPane.ERROR_MESSAGE);
                } else {
                    resultArea.setText("Thank you for completing the questionnaire!\n\n"
                            + "Name: " + name + "\n"
                            + "Age: " + age + "\n"
                            + "ADHD Filter: " + color);
                }
            }
        });

        // Make the frame visible
        frame.setVisible(true);
    }
}
