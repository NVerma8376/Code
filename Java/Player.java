import java.awt.*;
import javax.swing.*;

public class Player extends JPanel implements Runnable {

    private int x = 200;
    private int y = 200;
    private float inpe;
    private int mass = 3;
    private final float gravity = 9.8f;
    private int height;
    private float speedX = 2f;
    private float vel;
    private float speedY = 0;
    private int acc;

    private final int diameter = 50;

    public static void main(String[] args) {

        JFrame frame = new JFrame("Bouncing Ball");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Player bouncingBall = new Player();
        frame.add(bouncingBall);
        frame.setSize(600, 600);
        frame.setVisible(true);
        Thread thread = new Thread(bouncingBall);
        thread.start();

    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLUE);
        g.fillOval(x, y, diameter, diameter);
        g.fillOval(0, 0, WIDTH, HEIGHT);
        //g.fillOval(getHeight(), getWidth(), WIDTH, HEIGHT);
    }

    public void run() {
        while (true) {
            //speedY += gravity;
            //y += speedY;

            repaint();

            try {
                Thread.sleep(20);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
