import javax.swing.*;

public class Main {
    public static void main(String[]args){
        JFrame frame = new JFrame("Добрый день");
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.setBounds(100, 100, 500, 500);
        JLabel label = new JLabel("Shalooooooom");
        frame.add(label);

        frame.setVisible(true);

    }
}