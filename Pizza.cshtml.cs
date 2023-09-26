using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace starting_app.Pages {
  public class PizzaModel : PageModel {
    public string PizzaTotal (string pizzaType) {
      Dictionary<string, double> PizzaCost = new Dictionary<string, double>()
      {
        { "Cheese", 10 },
        { "Pepperoni", 11 },
        { "Vegetarian", 12 },
        { "PB", 15}
      };
      return "$" + String.Format("{0:0.00}", PizzaCost[pizzaType]);
    }

    public string Total {get; set;}
    public string Customer {get; set;}
    public string Order {get; set;}
    public bool ExtraCheese {get; set;}

    public void OnGet() {
      Customer = "Brant Gigas";
      Order = "Cheese";
      ExtraCheese = false;
      Total = PizzaTotal("Cheese");
    }
  }
}
