import java.util.ArrayList
import java.util.Comparator
import java.util.HashSet
import java.util.PriorityQueue

object QuebraCabeca {
  internal var CIMA = 1
  internal var BAIXO = 2
  internal var DIREITA = 3
  internal var ESQUERDA = 4
  internal var printOn = true
  internal var tamanho_fila = 0
  internal var tamanho_fila_max = 0
  internal var custo_solucao = 0.0
  internal var nos_expandidos = 0
  internal var dimensao = 3
  internal var solucao = intArrayOf(1, 2, 3, 4, 5, 6, 7, 8, 0)
  internal var inicio = intArrayOf(8, 4, 0, 5, 1, 7, 6, 2, 3)
  internal var fila = PriorityQueue(5, ComparadorNo())
  internal var processados:Set<*> = HashSet()

  @JvmStatic fun main(args:Array<String>) {
    val no = iniciarBusca(inicio)
    if (no != null)
    {
      imprimirResultado(no, true)
    }
    else
    {
      println("SOLUCAO NAO ENCONTRADA!")
    }
  }
  private fun iniciarBusca(posicoesIniciais:IntArray):No {
    val noInicial = No()
    noInicial.estado = posicoesIniciais
    fila.add(noInicial)
    tamanho_fila = 1
    while (!(fila.isEmpty()))
    {
      tamanho_fila--
      val no = fila.remove()
      if (goal(no.estado))
      {
        custo_solucao = no.custoCaminho
        return no
      }
      adicionarNosAlternativosFila(no)
      tamanho_fila = fila.size()
      if (tamanho_fila_max < tamanho_fila) tamanho_fila_max = tamanho_fila 
    }
    return null
  }

  private fun imprimirResultado(no:No, imprimeTabuleiros:Boolean) {
    print("ESTADO FINAL:")
    print("===============")
    imprimirTabuleiro(no)
    print("===============")
    print("tamanho_fila_max = " + tamanho_fila_max)
    print("nos_expandidos = " + nos_expandidos)
    print("===============")
    print("OPERACOES REVERSA:")
    while (no.pai != null)
    {
      print("===============")
      print("Step: " + no.step)
      print("Custo:" + no.custoCaminho)
      print("Acao:" + getAcaoReversa(no.acao))
      no = no.pai
      if (imprimeTabuleiros) imprimirTabuleiro(no)
    }
  }
  private fun getAcaoReversa(acao:Int):String {
    when (acao) {
      1 -> return "BAIXO"
      2 -> return "CIMA"
      3 -> return "ESQUERDA"
      4 -> return "DIREITA"
    }
    return "NENHUMA"
  }

  private fun imprimirTabuleiro(no:No) {
    if (!printOn) return
    for (i in 0 until dimensao)
    {
      imprimirTabuleiroLinha()
      for (j in 0 until dimensao)
      {
        val n = i * dimensao + j
        print("+ " + no.estado[n] + " ")
      }
      println("+")
    }
    imprimirTabuleiroLinha()
  }

  private fun imprimirTabuleiroLinha() {
    if (!printOn) return
    for (i in 0 until dimensao)
    {
      print("+---")
    }
    println("+")
  }

  private fun print(s:String) {
    if (printOn) println(s)
  }

  private fun heuristica(estado:IntArray):Double {
    val valor = 0.0
    for (i in 0 until dimensao)
    {
      for (j in 0 until dimensao)
      {
        val n = i * dimensao + j
        valor += (if (estado[n] == solucao[n]) 1 else 0).toDouble()
      }
    }
    return valor
  }
  private fun goal(estado:IntArray):Boolean {
    for (i in 0 until dimensao * dimensao)
    {
      if (estado[i] != solucao[i]) return false
    }
    return true
  }
  private fun recuperarSucessores(estado:IntArray):List<*> {
    val filhos = ArrayList()
    if (podeMoverCalhau(estado, CIMA))
    {
      val novoEstado = clonar(estado)
      moverCima(novoEstado)
      filhos.add(Sucessor(novoEstado, CIMA))
    }
    if (podeMoverCalhau(estado, ESQUERDA))
    {
      val novoEstado = clonar(estado)
      moverEsquerda(novoEstado)
      filhos.add(Sucessor(novoEstado, ESQUERDA))
    }
    if (podeMoverCalhau(estado, DIREITA))
    {
      val novoEstado = clonar(estado)
      moverDireita(novoEstado)
      filhos.add(Sucessor(novoEstado, DIREITA))
    }
    if (podeMoverCalhau(estado, BAIXO))
    {
      val novoEstado = clonar(estado)
      moverBaixo(novoEstado)
      filhos.add(Sucessor(novoEstado, BAIXO))
    }
    return filhos
  }
  private fun moverCima(estado:IntArray) {
    val pos = 0
    for (i in dimensao until dimensao * dimensao)
    {
      if (estado[i] == 0)
      {
        pos = i
        break
      }
    }
    if (pos > 0)
    {
      val valor = estado[pos - dimensao]
      estado[pos - dimensao] = 0
      estado[pos] = valor
    }
  }
  private fun moverBaixo(estado:IntArray) {
    val pos = 0
    for (i in 0 until dimensao * dimensao)
    {
      if (estado[i] == 0)
      {
        pos = i
        break
      }
    }
    val valor = estado[pos + dimensao]
    estado[pos + dimensao] = 0
    estado[pos] = valor
  }
  private fun moverEsquerda(estado:IntArray) {
    val pos = 0
    for (i in 0 until dimensao * dimensao)
    {
      if (estado[i] == 0)
      {
        pos = i
        break
      }
    }
    val valor = estado[pos - 1]
    estado[pos - 1] = 0
    estado[pos] = valor
  }
  private fun moverDireita(estado:IntArray) {
    val pos = 0
    for (i in 0 until dimensao * dimensao)
    {
      if (estado[i] == 0)
      {
        pos = i
        break
      }
    }
    val valor = estado[pos + 1]
    estado[pos + 1] = 0
    estado[pos] = valor
  }
  private fun adicionarNosAlternativosFila(no:No) {
    if (!(processados.contains(no.toString())))
    {
      processados.add(no.toString())
      val expandidos = expandirNos(no)
      for (o in expandidos)
      {
        fila.add(o)
      }
    }
  }
  private fun clonar(estado:IntArray):IntArray {
    val ret = IntArray(estado.size)
    for (i in estado.indices)
    {
      ret[i] = estado[i]
    }
    return ret
  }
  private fun expandirNos(no:No):List<*> {
    val nos = ArrayList()
    val proximos = recuperarSucessores(no.estado)
    for (prox in proximos)
    {
      val no0 = No()
      no0.pai = no
      no0.estado = prox.estado
      no0.step = no.step + 1
      no0.acao = prox.acao
      no0.custoStep = 1.0
      no0.custoCaminho += no0.pai.custoCaminho + 1.0
      nos.add(no0)
    }
    nos_expandidos++
    return nos
  }
  private fun podeMoverCalhau(estado:IntArray, acao:Int):Boolean {
    val posicao = 0
    for (i in 0 until dimensao * dimensao)
    {
      if (estado[i] == 0)
      {
        posicao = i
        break
      }
    }
    if (acao == ESQUERDA)
    {
      while (posicao >= 0)
      {
        if (posicao == 0) return false
        posicao -= dimensao
      }
    }
    else if (acao == CIMA)
    {
      if (posicao >= 0 && posicao < dimensao) return false
    }
    else if (acao == DIREITA)
    {
      posicao++
      while (posicao >= dimensao)
      {
        if (posicao == dimensao) return false
        posicao -= dimensao
      }
    }
    else if (acao == BAIXO)
    {
      if (posicao >= dimensao * (dimensao - 1)) return false
    }
    return true
  }
  internal class Sucessor(_estado:IntArray, _acao:Int) {
    var estado:IntArray
    var acao:Int = 0
    init{
      estado = _estado
      acao = _acao
    }
  }
  internal class No {
    var estado:IntArray
    var acao:Int = 0
    var pai:No
    var step = 0
    var custoCaminho = 0.0
    var custoStep = 0.0
    fun recuperarArvore():List<*> {
      val atual = this
      val ret = ArrayList()
      while (!(atual.pai != null))
      {
        ret.add(0, atual)
        atual = atual.pai
      }
      ret.add(0, atual)
      return ret
    }
    public override fun toString():String {
      val ret = ""
      for (i in 0 until dimensao * dimensao)
      {
        ret += estado[i]
      }
      return ret
    }
    public override fun equals(o:Any):Boolean {
      if ((o == null) || (this.javaClass != o.javaClass)) return false
      if (this === o) return true
      val x = o as No
      for (i in 0 until dimensao)
      {
        if (estado[i] != x.estado[i])
        {
          return false
        }
      }
      return true
    }
  }
  internal class ComparadorNo:Comparator<*> {
    fun compare(o1:No, o2:No):Int {
      val d1 = heuristica(o1.estado)
      val d2 = heuristica(o2.estado)
      return (d2 - d1).toInt()
    }
  }
}
