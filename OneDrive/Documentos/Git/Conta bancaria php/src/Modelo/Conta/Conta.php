<?php

namespace Gabriel\Banco\Modelo\Conta;

// atributos estáticos são atributos da classe e raros

class Conta 
{
    private $titular;
    private $saldo;
    private static $numeroDeContas = 0;

    public function __construct(Titular $titular)
    {
        $this->titular = $titular;
        $this->saldo = 0;
        
        self::$numeroDeContas++;
    }

    public function __destruct()
    {
        self::$numeroDeContas--;
    }
//cada método só faz uma coisa
//o método construtor serve para passar parametros obg não deixando null, logo, não precisa de setter
//inicializar instaância, sem muitas regras de negócios

    public function sacar(float $valorASacar): void
    {
        if ($valorASacar > $this->saldo) {
            echo "Saldo indisponível";
            return;
        }

        $this->saldo -= $valorASacar;
    }

    public function depositar(float $valorADepositar): void
    {
        if ($valorADepositar < 0) {
            echo "Valor precisa ser positivo";
            return;
        }
        
        $this->saldo += $valorADepositar; ##pode ser escrito dos dois jeitos, evitar else
    }

    public function transferir(float $valorATransferir, Conta $contaDestino): void
    {
        if ($valorATransferir > $this->saldo) {
            echo "Saldo indisponível";
            return;
        }

        $this->sacar($valorATransferir);
        $contaDestino->depositar($valorATransferir);
    }


    public function recuperarSaldo(): float
    {
        return $this->saldo;
    }

    public function recuperarNomeTitular(): string
    {
        return $this->titular->recuperarNome();
    }

    public function recuperarCpfTitular(): string
    {
        return $this->titular->recuperarCpf();
    }

//para organizar o código sem expor funcionalidade interna (tipo validação)
    
    public static function recuperarNumeroDeContas(): int
    {
        return self::$numeroDeContas;
    }
}
