 /*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
;

/**
 *
 * @author lorraine
 */
@WebServlet(urlPatterns = {"/Search"})
public class Search extends HttpServlet {

 
    @Override
    public void init(){
    
    }
       // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        //get the selection parameter if it exists
        String param1 = request.getParameter("param1");
        String param2 = request.getParameter("param2");
        String keyword = request.getParameter("search_term");
        String role = request.getParameter("role");
        
        StringBuilder sb = new StringBuilder();
       
        String finalSearch = sb.toString();
              
        
        if(finalSearch!=null){
             
               
        }else{
            
         
        }
      
       
    }

}
