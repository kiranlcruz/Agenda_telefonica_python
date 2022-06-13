<?php

require_once 'autoload.php';

use Gabriel\Banco\Modelo\Conta\Titular;
use Gabriel\Banco\Modelo\Endereco;
use Gabriel\Banco\Modelo\Cpf;
use Gabriel\Banco\Modelo\Conta\Conta;

$endereco = new Endereco('Petrópolis', 'um bairro', 'minha rua', '71B');
$vinicius = new Titular(new Cpf('123.456.789-10'), 'Vinicius Dias', $endereco);
$primeiraConta = new Conta($vinicius);
$primeiraConta->depositar(500);
$primeiraConta->sacar(300); // isso é ok

echo $primeiraConta->recuperarNomeTitular() . PHP_EOL;
echo $primeiraConta->recuperarCpfTitular() . PHP_EOL;
echo $primeiraConta->recuperarSaldo() . PHP_EOL;

$patricia = new Titular(new Cpf('698.549.548-10'), 'Patricia', $endereco);
$segundaConta = new Conta($patricia);
var_dump($segundaConta);

$outroEndereco = new Endereco('A', 'b', 'c', '1D');
$outra = new Conta(new Titular(new Cpf('123.654.789-01'), 'Abcdefg', $outroEndereco));
unset($segundaConta);
echo Conta::recuperarNumeroDeContas();