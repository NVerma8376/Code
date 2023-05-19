import javax.swing.*;
import java.awt.event.*;

class Gui implements ActionListener {

    JFrame frame = new JFrame("TestFrame");
    JButton button = new JButton("Click me");
    JTextField tf = new JTextField();

    Gui() {
        prepareGui();
        button();
        text();
    }

    public void prepareGui() {
        frame.setTitle("My Window");
        frame.getContentPane().setLayout(null);
        frame.setVisible(true);
        frame.setBounds(200, 200, 400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void button() {
        button.addActionListener(this);
        button.setBounds(200, 200, 100, 40);
        frame.add(button);
    }

    public void text() {
        tf.setBounds(200, 150, 100, 40);
        frame.add(tf);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        tf.setText("Hello World");

    }

}

public class GuiTesting {
    public static void main(String[] args) {
        new Gui();
    }
}