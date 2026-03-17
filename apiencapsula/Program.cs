
using API.Processador;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddOpenApi();
var app = builder.Build();
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}
app.UseHttpsRedirection();



Processador processador = new Processador();

app.MapGet("/{content}", (string content) =>
{
    return processador.transform(content);
})
.WithName("processar");

app.Run();
