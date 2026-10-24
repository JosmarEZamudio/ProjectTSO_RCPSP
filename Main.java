import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    
    public static void main(String[] args) throws IOException{

        Main hola  = new Main();

        hola.metodoExterno();
  
    }


//Metodo para usar codigo de python, ejecutarlo como proceso externo
    private void metodoExterno() throws IOException { 
        String frase = null;
        System.out.println("Escribe lo que quieras: ");
        try(BufferedReader lector = new BufferedReader(
            new InputStreamReader(System.in)
        );){

        frase = lector.readLine();
        }

        try{
            ProcessBuilder pyton = new ProcessBuilder(
                "C:\\Users\\josma\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe",
                "saludo.py",
                frase,
                "3",
                "5",
                "7",
                "7");

            pyton.redirectErrorStream(true);

            Process proceso = pyton.start();

            BufferedReader imprimir = new BufferedReader(
                new InputStreamReader(proceso.getInputStream())
            );

            String linea = null;

            while((linea = imprimir.readLine()) != null){
                System.out.println(linea);
            }

            int resultado = proceso.waitFor();

            System.out.println("Codigo de salida: " + resultado);


        }
        catch(Exception e){
            e.printStackTrace();
        }
    }

}