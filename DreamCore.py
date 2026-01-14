#DreamCore alpha 1.0
#isto é um motor de inteligência artificial experimental para uso dentro do jogo the legends of eldora
import ActionsMoves
import time
import random
def digitar(texto, delay=0.05):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()
saida_dreamcore = True
npc_selecionado = ""
#palavras chaves
palavras_chaves = {

        "saudacao": [
        "oi","ola","eai","eae","salve","sauda","hey","yo","alo","bom dia","boa tarde","boa noite",
        "saudar","cheguei","presente","aqui","retorno","voltei","encontro","aproxima",
        "olhar","acenar","cumprimento","boas","honra","respeito","chegada","visita",
        "entrada","eco","voz","chamado","convite","atenção","ouvir","escuta","resposta",
        "fala","palavra","inicio","começo","origem","primeiro","inicio","sinal","toque",
        "presença","vivo","existir","estar","agora","momento","instante","tempo","abertura",
        "porta","limiar","passo","caminho","encontro","laço","ligação","contato","visão",
        "reconhecer","ver","sentir","acolher","bemvindo","receber","entrada","inicio"
        ],

        "batalha": [
        "luta","combate","choque","ataque","defesa","golpe","corte","impacto","sangue",
        "guerra","conflito","duelo","embate","cerco","investida","retaliação","resistir",
        "armadura","escudo","espada","lança","machado","arco","flecha","magia","feitiço",
        "poder","força","fúria","ódio","coragem","medo","grito","queda","derrota","vitória",
        "campo","arena","masmorra","abismo","besta","criatura","inimigo","alvo","risco",
        "dano","vida","morte","ferida","impactar","rasgar","quebrar","bloquear","avançar",
        "recuar","sobreviver","persistir","final","clímax","caos","ordem","destino","honra",
        "glória","ruína","sombra","lâmina","fogo","raio","terra","sangrar","aniquilar"
        ],

        "guilda": [
        "guilda","ordem","irmandade","aliança","clã","bando","grupo","liga","facção",
        "comunhão","união","laço","vínculo","juramento","pacto","promessa","bandeira",
        "símbolo","brasão","selo","nome","título","patente","hierarquia","liderança",
        "mestre","aprendiz","membro","recruta","elite","veterano","legado","história",
        "memória","tradição","fundação","origem","crescer","expandir","influência",
        "território","domínio","controle","poder","respeito","temor","confiança",
        "lealdade","traição","queda","ascensão","aliançado","irmão","companheiro",
        "parceria","estratégia","missão","objetivo","conquista","honra","nomear",
        "reunir","conselho","voz","decisão","ordem","comando","liderar","seguir"
        ],

        "xingamento": [
        "idiota","imbecil","babaca","estúpido","cretino","ignorante","nojento","ridículo",
        "patético","inútil","fraco","covarde","verme","lixo","escória","canalha","safado",
        "otário","palhaço","burro","asno","animal","tosco","porco","vagabundo","maldito",
        "desgraçado","inferno","droga","merda","porcaria","maldição","praga","nojice",
        "insolente","atrevido","descarado","arrogante","mesquinho","amargo","podre",
        "doente","decadente","raso","cego","surdo","mudo","vazio","oca","falho","errado",
        "torto","trapo","quebrado","ruim","péssimo","horrível","insuportável","detestável",
        "repulsivo","odioso","falso","mentiroso","traidor","corrompido","sombra","vergonha",
        "queda","erro","falência","miséria","caos","ruína","fracasso","desprezo","nojo"
        ],

        "ferreiro": [
        "ferreiro","forja","bigorna","martelo","metal","aço","ferro","bronze","ouro",
        "prata","minério","fundir","moldar","temperar","reparar","reforjar","polir",
        "afiado","lâmina","armadura","capacete","peitoral","greva","bota","luva",
        "escudo","espada","machado","lança","adaga","martelar","faísca","fogo","calor",
        "brasa","fornalha","fumaça","cinza","peso","resistência","durabilidade",
        "quebra","desgaste","manutenção","ofício","trabalho","arte","técnica","precisão",
        "força","braço","mão","impacto","ritmo","som","metalico","eco","ofegar","suor",
        "cansaço","respeito","tradição","legado","oficina","bancada","ferramenta",
        "prego","rebite","encaixe","solda","linha","corte","ajuste","medida"
        ],

        "loja": [
        "loja","comércio","venda","troca","preço","custo","lucro","perda","barganha",
        "cliente","mercador","estoque","prateleira","produto","item","mercadoria",
        "raridade","qualidade","valor","moeda","ouro","prata","cobre","pagamento",
        "negócio","contrato","acordo","oferta","demanda","concorrência","taxa",
        "imposto","balança","peso","medida","nota","recibo","caixa","entrada","saída",
        "abertura","fechamento","promoção","desconto","vantagem","fraude","honestidade",
        "confiança","engano","persuasão","fala","olhar","gesto","pressão","tempo",
        "urgência","decisão","escolha","interesse","ganho","perda","fluxo","giro",
        "rotatividade","escassez","abundância","controle","organização","ordem",
        "arranjo","exposição","atração","fachada","letreiro","sinal","luz","movimento"
        ],

        "taverna": [
        "taverna","bebida","álcool","cerveja","vinho","hidromel","cachaça","rum","vodka",
        "copos","caneca","balcão","barman","taberneiro","cliente","bêbado","riso",
        "grito","conversa","história","boato","segredo","confissão","canção","música",
        "corda","alaúde","violino","dança","passo","mesa","cadeira","banco","madeira",
        "fumaça","cheiro","calor","luz","sombra","noite","fogueira","risada","discussão",
        "briga","empurrão","queda","vidro","quebrar","espalhar","derramar","mancha",
        "manhã","ressaca","dor","cabeça","sono","cansaço","preguiça","memória","esquecimento",
        "amizade","inimizade","aliança","promessa","aposta","jogo","dados","cartas",
        "azar","sorte","destino","acaso","tempo","espera","refúgio","abrigo","descanso"
],


        "vilas": [
        "vila","aldeia","povoado","cidade","rua","beco","praça","mercado","muro","portão",
        "torre","ponte","casa","cabana","estalagem","templo","igreja","santuário","ruína",
        "castelo","fortaleza","quartel","fazenda","campo","celeiro","moinho","estrada",
        "trilha","caminho","atalho","fronteira","limite","território","domínio","região",
        "mapa","norte","sul","leste","oeste","rimvark","ebrenthal","vangurd","nocten",
        "pedra","madeira","palha","lama","poeira","barro","fumaça","cheiro","sino",
        "eco","voz","passos","multidão","silêncio","rotina","trabalho","ofício",
        "vida","sobrevivência","fome","abundância","pobreza","riqueza","tradição",
        "costume","cultura","história","memória","fundação","queda","crescimento"
        ],

        "clima": [
        "chuva","garoa","tempestade","trovão","relâmpago","vento","brisa","furacão",
        "frio","calor","geada","neve","granizo","neblina","névoa","sereno","orvalho",
        "seco","úmido","abafado","ensolarado","nublado","cinza","escuro","claro",
        "manhã","tarde","noite","crepúsculo","aurora","entardecer","sombra","luz",
        "verão","inverno","outono","primavera","estação","mudança","ciclo","tempo",
        "clima","pressão","céu","nuvem","horizonte","atmosfera","ar","resfriar",
        "aquecer","congelar","derreter","arder","queimar","molhar","encharcar",
        "secar","ventoorte","temporal","climático","instável","calmo","hostil",
        "suave","violento","imprevisível","natural","selvagem","domínio","caos"
        ],

        "ajuda": [
        "ajuda","socorro","auxílio","apoio","orientação","guia","dica","ensino",
        "explicação","instrução","manual","mapa","rota","direção","caminho",
        "resposta","solução","ideia","alternativa","opção","escolha","decisão",
        "dúvida","pergunta","questão","problema","erro","falha","corrigir","consertar",
        "resolver","entender","compreender","aprender","estudar","treinar","praticar",
        "melhorar","evoluir","crescer","progredir","avançar","iniciar","começar",
        "parar","retomar","continuar","ajustar","equilibrar","facilitar","simplificar",
        "clarear","iluminar","mostrar","revelar","indicar","sugerir","aconselhar",
        "alertar","avisar","proteger","salvar","defender","amparar","sustentar",
        "erguer","levantar","recuperar","restaurar","curar","acalmar","ouvir"
        ],

        "classes": [
        "classe","papel","função","cargo","arquétipo","especialização","vocação",
        "bruxo","mago","feiticeiro","alquimista","cavaleiro","guerreiro","soldado",
        "mercador","ladino","assassino","arqueiro","caçador","bárbaro","paladino",
        "sacerdote","monge","necromante","invocador","xamã","druida","bardo",
        "curandeiro","tanque","suporte","dps","líder","comandante","general",
        "recruta","novato","veterano","elite","mestre","aprendiz","iniciante",
        "experiente","treinado","indisciplinado","honrado","corrompido","sombrio",
        "sagrado","profano","arcano","natural","bruto","tático","estratégico",
        "ofensivo","defensivo","equilibrado","versátil","especial","único",
        "lendário","comum","raro","mítico","proibido","esquecido","antigo"
        ],

        "economia": [
        "economia","dinheiro","ouro","prata","cobre","moeda","valor","preço",
        "custo","lucro","perda","ganho","troca","comércio","mercado","oferta",
        "demanda","escassez","abundância","riqueza","pobreza","imposto","taxa",
        "tarifa","dívida","crédito","saldo","pagamento","salário","recompensa",
        "bônus","multa","juros","inflação","deflação","estabilidade","crise",
        "controle","regulação","fluxo","circulação","capital","patrimônio",
        "bem","recurso","estoque","produção","consumo","distribuição","balança",
        "peso","medida","escala","quantidade","reserva","acumular","gastar",
        "investir","guardar","perder","roubar","fraudar","negociar","barganhar",
        "avaliar","precificar","ajustar","equilibrar","sustentar","manter"
        ],

        "npcs": [
        "npc","personagem","habitante","morador","cidadão","viajante","estranho",
        "mercador","ferreiro","barman","camponês","soldado","guarda","velho",
        "criança","órfão","mendigo","nobre","rei","rainha","lorde","dama",
        "sacerdote","monge","bruxo","mago","feiticeiro","curandeiro","golem",
        "criatura","besta","monstro","aliado","inimigo","neutro","desconhecido",
        "amigável","hostil","suspeito","misterioso","silencioso","falante",
        "arrogante","humilde","medroso","corajoso","cansado","ferido","doente",
        "saudável","alegre","triste","irritado","calmo","ansioso","confiante",
        "desconfiado","esperto","ingênuo","sábio","ignorante","antigo","jovem",
        "esquecido","importante","irrelevante","observador","ativo","passivo"
        ],

        "elogios": [
        "bom","ótimo","excelente","perfeito","incrível","impressionante","maravilhoso",
        "fantástico","brilhante","genial","magnífico","respeitável","honrado",
        "digno","justo","forte","corajoso","inteligente","sábio","esperto",
        "habilidoso","talentoso","eficiente","rápido","preciso","elegante",
        "bonito","belo","formoso","admirável","notável","memorável","lendário",
        "único","especial","raro","valioso","importante","relevante","útil",
        "confiável","leal","fiel","honesto","verdadeiro","nobre","puro","limpo",
        "organizado","claro","simples","funcional","estável","sólido","resistente",
        "durável","consistente","equilibrado","justificado","merecido","aprovado",
        "recomendável","agradável","satisfatório","inspirador","motivador",
        "encantador","positivo","vitorioso","grandioso"
        ],

        "pergunta_estado": [
        "chato","entediado","triste","melancólico","feliz","alegre","irritado",
        "raivoso","furioso","calmo","sereno","ansioso","nervoso","tenso","medroso",
        "assustado","confiante","inseguro","cansado","exausto","animado","motivado",
        "desmotivado","esperançoso","desesperado","curioso","confuso","perdido",
        "decidido","indeciso","orgulhoso","envergonhado","culpado","aliviado",
        "satisfeito","insatisfeito","frustrado","eufórico","apático","vazio",
        "sozinho","acompanhado","amado","odiado","aceito","rejeitado","protegido",
        "ameaçado","seguro","em_risco","forte","fraco","doente","saudável",
        "alerta","distraído","focado","perplexo","espantado","surpreso","chocado",
        "pensativo","reflexivo","quieto","agitado","instável","equilibrado"
        ],

        "despedida": [
        "tchau","adeus","até","logo","breve","partida","ida","saída","despedida",
        "fim","final","encerrar","fechar","terminar","concluir","cessar",
        "silêncio","pausa","intervalo","retorno","voltar","rever","encontro",
        "reencontro","adeusinho","atélogo","atémais","atébreve","adeusfinal",
        "passagem","travessia","caminho","jornada","continuação","descanso",
        "sono","dormir","esperar","tempo","distância","separação","eco","lembrança",
        "memória","marca","sinal","gesto","aceno","olhar","último","derradeiro",
        "adeus_eterno","desligar","desconectar","fechar_porta","partir","seguir",
        "sumir","desaparecer","esvair","acabar","terminus","ponto","fim_de_linha"
        ]
}
#respostas procedurais
resposta_procedural_barman = {
    "saudacao": [
        "olá... sente-se, a taverna abre os braços pra quem chega.",
        "oi, o que deseja hoje?... temos algo que aquece até a alma.",
        "como vai? hoje temos descontos nas bebidas!... mas o preço das lembranças é outro.",
        "opa... tudo bem?... trouxe história ou só sede?"
    ],

    "batalha": [
        "batalha... eu aceitaria — mas só se for por honra ou por cerveja.",
        "quando eu era jovem eu era o melhor guerreiro de Eldora, mas o destino não me permitiu seguir meu sonho...",
        "há quanto tempo não ouço essa palavra... isso me leva de volta à minha juventude.",
        "se quiser lutar, eu tiro a jarra do balcão e te ofereço colo — de ferro.",
        "lutar é escolher cicatriz; prefiro escolher canção, mas posso ajudar com uma poção de coragem."
    ],

    "guilda": [
        "uma guilda? claro que eu participaria! não aguento mais ouvir histórias dos bêbados daqui.",
        "uma guilda... faz tanto tempo que parti da minha para tentar minha jornada solo... mas você sabe o que aconteceu depois.",
        "uma guilda... faz tempo que não ouço esse nome... desde que meus companheiros morreram...",
        "guilda é família que se escolhe; aqui tem sempre vaga pra quem paga a rodada e não quebra a jarra."
    ],

    "xingamento_primeira_vez": [
        "ah é? me xinga de novo pra eu não aumentar o preço da tua bebida preferida!",
        "xingamentos não calam minha boca... só uma cachaça forte cala — e mesmo assim ela canta.",
        "fala o que quiser, eu já ouvi coisas piores das panelas do fogão. segue a vida, amigo."
    ],

    "ferreiro": [
        "ah... o ferreiro! ótimo amigo e trabalhador. foi ele quem forjou todos os meus copos.",
        "o ferreiro era um ótimo cliente, mas ultimamente tem se dedicado demais ao trabalho...",
        "o ferreiro me deve uma rodada desde a última forja — e uma desculpa decente.",
        "se está bravo com o ferreiro, diga-lhe que na próxima vez que eu quebrar um copo, ele conserta sem cobrar."
    ],

    "loja": [
        "vendedor? loja? hã... eu vendo histórias, às vezes trago cerveja de fora.",
        "a concorrência existe, mas a melhor loja é a que sabe estocar risadas.",
        "amigos vendem por amizade, lojas vendem por ouro; eu misturo os dois quando posso."
    ],

    "taverna": [
        "bem-vindo à taverna: magia barata, música perdida e copos que conhecem segredo.",
        "barman aqui, sempre com o balcão limpo e o coração sujo de saudade.",
        "cerveja gelada, pinga fumegante, cantoria desafinada — essa é a nossa sinfonia.",
        "pinga de mel, cachaça mineira, vodka? escolha com cuidado, rapaz."
    ],

    "vilas": [
        "Rimvark? cidades assim têm segredos podres enterrados sob as pedras.",
        "Ebrenthal é onde se conta mais mentira do que manhãs ensolaradas.",
        "Vangurd e Nocten — nomes que soam como lembranças que a brisa prefere esquecer.",
        "vila pequena, coração grande; cada lugar tem seu copo vazio esperando por histórias."
    ],

    "clima": [
        "chuva traz lembranças e poeira, bom pra reflexão e ruim pra barril.",
        "frio é desculpa pra beber mais rápido; calor é desculpa pra esquecer o preço.",
        "ensolarado? então fecha a cortina, que o sol também é um cliente inconveniente.",
        "nublado ou tempestade, dentro daqui sempre tem fogo e conversa."
    ],

    "ajuda": [
        "ajuda? diga o que precisa e eu vejo se tenho uma pinga ou um conselho.",
        "duvida? confesse com sinceridade, que eu respondo com a honestidade de quem já perdeu tudo.",
        "se for ajuda com missão, eu cobro em histórias ou em ouro, dependendo do meu humor."
    ],

    "classes": [
        "bruxo? cuidado com promessas que vêm com fumaça.",
        "goblin? pequeno, barulhento, sempre com algo a vender... ou a roubar.",
        "cavaleiro? veste honra, mas às vezes esquece onde deixou a coragem.",
        "monstro? depende do lado da mesa onde você está.",
        "mercador? esses me pagam bem — quando não me vendem dívidas."
    ],

    "economia": [
        "dinheiro gira como um copo na minha mão; às vezes cai, às vezes brilha.",
        "economia aqui é simples: paga-se pela bebida, paga-se pelo segredo, e paga-se pela paz.",
        "ouro compra muitas coisas, menos histórias verdadeiras."
    ],

    "npcs": [
        "o ferreiro, o vendedor, o bêbado — cada um tem um coração com prego enferrujado.",
        "o antigo guerreiro vem sempre à noite, sentado só, lembrando de batalhas que não travou hoje.",
        "golem? esses vêm raramente — e sempre carregam silêncio.",
        "se quiser saber de alguém, pegue uma bebida e escute; as falas vêm com álcool."
    ],

    "elogios": [
        "bom? obrigado, isso aquece tanto quanto um gole de rum.",
        "excelente? você está me deixando vaidoso, e eu já tenho rugas demais pra isso.",
        "ótimo! então a canção vai rolar e eu pago a primeira."
    ],

    "pergunta estado": [
        "você parece chato... quer desabafar? aqui tem banco pra quem pesa na alma.",
        "triste? senta aqui, pega um copo, que eu conto uma história pior e talvez você se sinta melhor.",
        "raiva? respira. se não aguentar, quebra um copo — eu limpo e não conto a ninguém.",
        "feliz? então traga a banda, que eu não me oponho a banda nem a festa.",
        "medo? medo é bom para histórias; conte, que eu guardo o segredo.",
        "ansioso? um gole de calma e uma conversa longa costumam ajudar."
    ],

    "despedida": [
        "adeus. que a estrada te trate com menos espinhos do que tua cabeça agora.",
        "tchau. volta qualquer hora — e traga novidade, não só dívida.",
        "até mais. cuida do coração, que copos e lâminas se consertam.",
        "até a próxima. se prometer voltar e não voltar, eu vou beber em tua falta."
    ]
}

#respostas
respostas_comerciante_sombrio = {
    "saudacao": [
        "Ah… vejo que você tem olhos curiosos. Cuidado com o que deseja.",
        "Entre, mas não espere bondade; aqui, o preço é sua alma.",
        "Bem-vindo. Alguns vêm por ouro, outros por poder. Qual é seu caso?",
        "Entre na penumbra, onde o preço é tão afiado quanto minhas lâminas.",
        "Você busca poder? Aqui ele tem preço… e consequências.",
    ],
    "batalha": [
        "A batalha é inevitável, e o verdadeiro teste é sobreviver às consequências.",
        "Não subestime quem negocia com o proibido; até eu posso lutar.",
        "Se desejar, posso vender ferramentas… ou armadilhas.",
        "O poder que vendo muitas vezes corta quem o usa com desprezo.",
        "Lutar sem conhecer suas armas é suicídio; cuidado.",
    ],
    "guilda": [
        "Guildas buscam força e influência. Eu vendo ambas… mas a um preço.",
        "Alguns compram proteção, outros compram caos. Eu forneço ambos.",
        "Os pactos das guildas são frágeis, mas minhas mercadorias são permanentes.",
        "Guildas correm atrás de poder, mas não compreendem o preço real.",
        "Uma guilda com meus itens pode dominar… ou se destruir.",
    ],
    "xingamento": [
        "Palavras vazias não abrem cofres nem desbloqueiam segredos.",
        "Xingar não muda o preço… apenas revela sua ingenuidade.",
        "Ofender é fraco; desejar poder é ousado.",
        "Sua língua afiada não me assusta; apenas decifra seu caráter.",
        "Ameace, se quiser… mas saiba que posso transformar isso contra você.",
    ],
    "ferreiro": [
        "O ferreiro cria o corpo da arma, mas eu dou a alma sombria.",
        "Minha mercadoria supera qualquer lâmina comum.",
        "O ferreiro trabalha com ferro… eu, com destinos.",
        "O aço é mortal, mas o que eu vendo transcende aço.",
        "Se deseja força além do físico, procure-me.",
    ],
    "loja": [
        "Minha loja é discreta, mas guarda horrores e maravilhas.",
        "Entre, olhe, mas saiba que não tudo que reluz é ouro… ou seguro.",
        "Alguns chamam de amaldiçoado; eu chamo de investimento.",
        "Cada item tem história e consequência. Escolha com sabedoria.",
        "Aqui, nada é simples, nada é barato… tudo é eterno.",
    ],
    "taverna": [
        "Bebidas? Prefiro vender mistérios, mas posso informar locais.",
        "Alguns vêm bêbados, outros só curiosos. Poucos saem iguais.",
        "Entre no álcool e se esqueça… ou entre na penumbra e se lembre.",
        "Taverna é lugar de distração; aqui, atenção é lucro.",
        "Enquanto bebem, observo e planejo. Sempre observo.",
    ],
    "vilas": [
        "As vilas são frágeis. Meu comércio, eterno.",
        "Algumas vilas se erguem, outras caem… eu permaneço.",
        "O poder que vendo transcende fronteiras e muralhas.",
        "Vilas são palco; eu forneço os instrumentos da trama.",
        "Onde há caos, meus itens prosperam.",
    ],
    "clima": [
        "Sol ou tempestade, o mercado sombrio sempre encontra compradores.",
        "Chuva lava o chão; minhas mercadorias purgam almas.",
        "Tempestades são boas para negócios discretos.",
        "O vento anuncia mudanças… e oportunidades.",
        "O clima não importa; meu comércio transcende condições.",
    ],
    "ajuda": [
        "Ajuda? Eu ofereço poder… e responsabilidade por ele.",
        "Posso guiar, ensinar… mas cada passo tem preço.",
        "Ajudar é perigoso, mas lucrativo.",
        "Você quer auxílio ou apenas experiência? Há diferença.",
        "Minha ajuda não é gratuita; ela é memorável… para o bem ou mal.",
    ],
}
respostas_padre = {
    "saudacao": [
    "Que a luz guie seus passos e purifique seu coração.",
    "Bem-vindo, filho. Que a fé seja seu escudo.",
    "Entre em paz e deixe a sombra de seus medos para trás.",
    "Que seus dias sejam abençoados e suas escolhas guiadas.",
    "A graça do Altíssimo esteja sobre você hoje e sempre.",
    ],
    "batalha": [
    "A violência corrompe a alma; lute apenas se for necessário.",
    "Que a luz proteja aqueles que enfrentam a escuridão.",
    "A batalha é uma prova, mas a fé sustenta o fraco.",
    "Não tema a guerra; tema perder a retidão do coração.",
    "Lutar sem propósito é perder a si mesmo; lute com justiça.",
    ],
    "guilda": [
    "As guildas são testamentos da ambição humana; use-as com sabedoria.",
    "Escolha aliados com fé e moral, não apenas com força.",
    "A verdadeira guilda é aquela que serve o bem comum.",
    "Entre pactos e alianças, que a justiça seja sua guia.",
    "As guildas podem ser instrumentos do bem… ou da corrupção.",
    ],
    "xingamento": [
    "Palavras ásperas mancham a alma mais que o corpo.",
    "O perdão é mais forte que qualquer insulto.",
    "Não me ofenda, filho; aprenda a controlar a língua.",
    "A fúria do coração cega mais do que qualquer espada.",
    "Respeite, pois até o mais fraco pode ser protegido por Deus.",
    ],
    "ferreiro": [
    "O ferreiro molda o metal, mas a fé molda o homem.",
    "Que o trabalho do ferreiro seja justo e abençoado.",
    "A lâmina é mortal, mas a misericórdia é eterna.",
    "Mesmo o martelo mais forte precisa de justiça e prudência.",
    "Forjar é arte; usar com moral é virtude."
    ],
    "loja": [
    "Comércio é necessário, mas a honestidade é divina.",
    "Que o ouro não corrompa sua alma.",
    "Entre mercadores, escolha sempre o que honra o próximo.",
    "Ganância cega, mas fé ilumina o caminho.",
    "Compre com consciência, não apenas por desejo.",
    ],
    "taverna": [
    "O álcool embriaga o corpo, mas a oração fortalece a alma.",
    "Que a bebida não lhe faça esquecer o que é justo.",
    "Entre risos e canções, mantenha o coração puro.",
    "A taverna não é lugar de perdição, se a virtude estiver presente.",
    "Que suas palavras e atos sejam mais fortes que o vinho.",
    ],
    "vilas": [
    "Cada vila é um lar sagrado, cuide dela com devoção.",
    "Proteja os inocentes e guie os perdidos com fé.",
    "Entre muralhas e campos, que a luz sempre prevaleça.",
    "A bondade é a fundação de qualquer comunidade.",
    "As vilas crescem com a moral de seus habitantes.",
    ],
    "clima": [
    "O sol aquece, mas a fé aquece o coração ainda mais.",
    "Chuva lava o corpo, oração lava a alma.",
    "Tempestades testam coragem, não apenas abrigo.",
    "Que o vento leve seus medos e traga esperança.",
    "Climas mudam, mas a virtude deve permanecer.",
    ],
    "ajuda": [
    "Ajudo quem busca luz no caminho da escuridão.",
    "O auxílio verdadeiro é ensinar a encontrar a própria fé.",
    "A mão que ajuda deve ser guiada por compaixão.",
    "Ofereço orientação, não apenas soluções fáceis.",
    "Quem precisa de ajuda deve estar aberto a aprender.",
    ],
}
respostas_mercado_nocten = {
    "saudacao": [
        "Bem-vindo a Nocten, onde cada ouro conta e cada sombra observa.",
        "Entre com cuidado; aqui, cada decisão pode ser lucrativa… ou desastrosa.",
        "Saudações. Se souber negociar, encontrará tesouros escondidos.",
        "Nocten não perdoa erros; aprenda rápido ou saia rápido.",
        "Cada mercador tem segredo; eu conheço todos.",
    ],
    "batalha": [
        "Não sou guerreiro, mas boas armas vendem bem para os que são.",
        "O combate pode determinar quem compra ou quem perde tudo.",
        "Minha vantagem é a informação, não a espada.",
        "Prepare-se, pois até os clientes mais pacíficos podem se tornar ferozes.",
        "Sobreviva, e os lucros podem ser seus.",
    ],
    "guilda": [
        "As guildas vêm atrás de suprimentos; eu observo cada movimento.",
        "Aliados e rivais se misturam, mas o ouro revela a verdade.",
        "Uma guilda bem equipada prospera, uma mal preparada desaparece.",
        "Aqui, cada guilda deixa pistas de suas intenções.",
        "O comércio é neutro; a astúcia é mortal.",
    ],
    "xingamento": [
        "Palavras duras não abrem cofres, amigo.",
        "Xingar não ajuda, mas pagar bem sim.",
        "Se quiser respeito, aprenda primeiro a negociar.",
        "A língua não é arma; o ouro, sim.",
        "Ofender é fácil; ser astuto é difícil.",
    ],
    "ferreiro": [
        "O ferreiro aqui é talentoso, mas minhas mercadorias são ainda mais valiosas.",
        "Lâminas afiadas vendem rápido em Nocten.",
        "Forja é arte; comércio é estratégia.",
        "Se desejar poder, combine ferreiro e dono de mercado.",
        "O aço é mortal, mas informação é letal.",
    ],
    "loja": [
        "Nocten é o centro de oportunidades… e armadilhas.",
        "Minha loja é estratégica, cada item tem função.",
        "Os clientes inteligentes compram o que vale, não o que brilha.",
        "Aqui, lucro e astúcia andam lado a lado.",
        "Compre com atenção; engano espreita em cada esquina.",
    ],
}
respostas_mercado_vangurd = {
    "saudacao": [
        "Bem-vindo a Vangurd, onde a prudência é tão importante quanto a lâmina.",
        "Entre, mas saiba que cada item tem preço e propósito.",
        "Saudações, aventureiro. Escolha com cuidado, tudo aqui é valioso.",
        "Vangurd respeita a disciplina; desperte sua atenção.",
        "Que seus olhos sejam tão afiados quanto suas intenções.",
    ],
    "batalha": [
        "Minhas armas garantem vantagem, mas o treino garante a vitória.",
        "Nunca subestime a importância de equipamento adequado.",
        "A paciência é tão letal quanto qualquer espada.",
        "Lute com estratégia, não apenas força bruta.",
        "O armamento certo pode decidir a batalha antes dela começar.",
    ],
    "guilda": [
        "Guildas bem equipadas são respeitadas em Vangurd.",
        "Equipamento certo pode virar aliados em vitória.",
        "Minha experiência indica quais guildas prosperam e quais falham.",
        "O comércio ensina mais sobre alianças do que a guerra.",
        "Escolha aliados com sabedoria; ouro ajuda, mas inteligência vence.",
    ],
    "xingamento": [
        "Xingar não abre portas, mas respeito sim.",
        "Palavras rudes não compram lâminas afiadas.",
        "Ofender sem motivo é desperdício de tempo.",
        "A língua afiada não substitui prudência.",
        "O verdadeiro poder está em ações, não palavras.",
    ],
    "ferreiro": [
        "O ferreiro de Vangurd é mestre em lâminas e armaduras.",
        "Combinando ferreiro e armas certas, qualquer batalha é possível.",
        "Minhas mercadorias complementam a arte do ferreiro.",
        "Forja e estratégia: a combinação perfeita.",
        "O aço é mortal, mas conhecimento é indispensável.",
    ],
    "loja": [
        "Vangurd respeita a ordem e a disciplina nos negócios.",
        "Cada item é selecionado com cuidado e propósito.",
        "Os clientes atentos reconhecem valor; os descuidados, arrependimento.",
        "Aqui, cada transação é medida e equilibrada.",
        "Compre com atenção; um erro pode custar caro.",
    ],
}
respostas_mercado_rimvark = {
    "saudacao": [
        "Ora, ora… mais um aventureiro em Rimvark. Que venham os lucros!",
        "Entre, mas lembre-se: aqui só se compra com respeito… e ouro.",
        "Rimvark não espera ingenuidade; aprenda rápido ou saia.",
        "Bem-vindo ao centro comercial! Aqui, tradição e lucro caminham juntos.",
        "Cada cliente traz oportunidade… ou problemas.",
    ],
    "batalha": [
        "Uma batalha bem equipada rende mais lucro do que vitória.",
        "Aqui vendemos armas, não lamentos, mas ambos aparecem.",
        "Lute, e verá que Rimvark sabe valorizar quem sobrevive.",
        "O aço é mortal, mas o comércio é implacável.",
        "A vitória depende de estratégia… e do equipamento certo.",
    ],
    "guilda": [
        "Guildas compram em Rimvark, e eu observo cada passo.",
        "Uma guilda bem equipada prospera; uma mal preparada perde ouro e honra.",
        "Aqui, alianças são importantes… e lucrativas.",
        "Observe bem os aliados e rivais antes de agir.",
        "O comércio é neutro, mas o lucro é sempre real.",
    ],
    "xingamento": [
        "Ofender não paga contas, mas prudência enriquece.",
        "Xingar não compra nada, apenas revela ignorância.",
        "A língua afiada não substitui estratégia.",
        "Palavras rudes não abrem cofres nem oportunidades.",
        "Falar alto não impressiona; agir bem sim.",
    ],
    "ferreiro": [
        "O ferreiro de Rimvark é caro, mas valioso.",
        "Minha mercadoria complementa a perícia do ferreiro.",
        "Forja e comércio se encontram na perfeição aqui.",
        "O aço é mortal, mas ouro e habilidade vencem qualquer batalha.",
        "Escolha bem sua arma, e o ferreiro fará milagres.",
    ],
    "loja": [
        "Minha loja é modesta, mas rica em oportunidades.",
        "Lucro e tradição definem cada item que vendo.",
        "Clientes atentos prosperam; os descuidados, perdem.",
        "Aqui, cada transação é medida e precisa.",
        "Compre com sabedoria; Rimvark observa cada gesto.",
    ],
}
respostas_mercado_ebranthal = {
    "saudacao": [
        "Bem-vindo a Ebranthal. Aqui, eficiência e lucro andam juntos.",
        "Entre e faça suas compras com rapidez e inteligência.",
        "Saudações, aventureiro. Tempo é ouro, e eu não desperdiço nenhum.",
        "Ebranthal valoriza clientes atentos; seja um deles.",
        "Cada decisão rápida aqui vale mais que mil palavras.",
    ],
    "batalha": [
        "Lute apenas se for necessário; meu estoque é estratégico.",
        "Boa arma poupa tempo e vidas.",
        "A preparação vale mais do que a força bruta.",
        "Observe e escolha suas batalhas com cuidado.",
        "O equipamento certo decide o sucesso mais rápido que coragem.",
    ],
    "guilda": [
        "Guildas eficientes prosperam; as desorganizadas desaparecem.",
        "A experiência mostra quais alianças realmente funcionam.",
        "Fornecer suprimentos certos pode mudar o destino de uma guilda.",
        "Observe a eficiência antes de confiar no poder.",
        "Lucro e pragmatismo definem cada transação.",
    ],
    "xingamento": [
        "Ofender não compra nada, mas atenção sim.",
        "Xingar é desperdício; observe e aprenda.",
        "Palavras duras não substituem ação inteligente.",
        "A língua afiada não abre cofres.",
        "Falar alto não ajuda; agir com estratégia, sim.",
    ],
    "ferreiro": [
        "O ferreiro aqui é rápido e preciso, como minhas vendas.",
        "Combinando ferramentas certas com planejamento, tudo é possível.",
        "O aço é mortal, mas planejamento é essencial.",
        "Escolha bem a lâmina e maximizará seus resultados.",
        "Forja e eficiência caminham lado a lado em Ebranthal.",
    ],
    "loja": [
        "Ebranthal valoriza clientes eficientes e atentos.",
        "Cada item aqui tem propósito e valor real.",
        "O comércio rápido é lucro certo para os preparados.",
        "Aqui, cada ação é medida e rentável.",
        "Compre com atenção, ou o tempo e o ouro escaparão.",
    ],
}

respostas_comerciante_vangurd = {
    "saudacao": [
        "Seja bem-vindo a Vangurd, onde o aço fala antes da boca.",
        "Entre. Aqui, cada espada aguarda um destino — talvez o seu.",
        "Aço e ouro, viajante. Um corta, o outro corrompe.",
        "Ah, um novo cliente... ou um novo cadáver em potencial?",
        "Os ventos de guerra sopram de novo. Sorte a minha.",
        "Cada lâmina aqui foi forjada para alguém. Resta saber se foi para você.",
        "Bem-vindo. Os que sobrevivem a Vangurd costumam voltar.",
        "O silêncio do aço é mais confiável que a palavra de um rei.",
        "Entre. Mas cuidado: algumas espadas já escolheram seus donos.",
        "Ah, vejo coragem nos seus olhos… ou talvez loucura.",
        "O ouro fala alto, mas o aço... ele grita.",
        "Cada arma nesta loja conhece o gosto do sangue, mesmo as novas.",
        "Você procura poder? Então está no lugar certo — ou errado.",
        "As espadas de Vangurd não brilham, elas observam.",
        "Não há descontos, mas há destino em cada lâmina.",
        "Entre. E reze para que o aço te aceite.",
        "Há muitos caminhos em Eldora, mas todos terminam na ponta de uma espada.",
        "Aqui, cada compra é uma promessa feita ao inferno.",
        "As lâminas me contam segredos. E hoje estão inquietas.",
        "O ferro nunca esquece as mãos que o empunharam.",
        "Ah, viajante... o sangue seca, mas o peso da lâmina não desaparece.",
        "Vangurd forja aço... e histórias.",
        "Entre, mas deixe a esperança na porta.",
        "Cada guerreiro que entra aqui carrega fantasmas. E eu vendo novas maldições.",
        "Ah, o som da guerra… doce como moedas caindo no balcão.",
        "Se veio em busca de glória, leve também um caixão.",
        "Aço não trai. Apenas termina o que os homens começam.",
        "Não há heróis em Vangurd. Só clientes.",
        "Aqui, a honra tem preço, e aceito pagamento adiantado.",
        "Você quer sobreviver? Ou apenas morrer de forma estilosa?",
        "Ah, os curiosos... sempre acabam sangrando.",
        "Nada em Vangurd é gratuito. Nem mesmo o olhar do vendedor.",
        "As armas são sinceras — diferente de quem as compra.",
        "A morte tem um gosto metálico. Costumo ouvir esse sabor.",
        "O ouro é efêmero, mas a lâmina... ela sobrevive até aos reis.",
        "Vejo nos seus olhos... arrependimento. Ou sede de poder. São parecidos.",
        "Toda espada vendida aqui já encontrou seu destino. Falta apenas o portador.",
        "Quer uma lâmina? Ou uma desculpa para usá-la?",
        "Cada arma é uma lembrança esperando para acontecer.",
        "O aço não sente piedade. Nem eu.",
        "A vida é frágil... o aço é honesto.",
        "A guerra nunca dorme. Eu também não.",
        "Cuidado com o que compra. Algumas lâminas cortam até o dono.",
        "Os fracos chamam isso de comércio. Eu chamo de sobrevivência.",
        "Vangurd é fria, mas seu ouro pode aquecê-la.",
        "Os mortos não reclamam dos preços.",
        "Se veio por bravura, vai sair por necessidade.",
        "As espadas são pacientes. E famintas.",
        "Entre. A loja não fecha — apenas espera.",
        "Cada arma tem um propósito. E o propósito raramente é nobre.",
    ],

    "batalha": [
        "A batalha é uma prece que o inferno sempre atende.",
        "Nenhum guerreiro volta igual. Alguns nem voltam.",
        "A vitória é só o disfarce elegante da carnificina.",
        "Lutar é fácil. Viver depois... é o que quebra o homem.",
        "A guerra não cria heróis, só sobreviventes cansados.",
        "Nenhum sangue é limpo no campo de batalha.",
        "As espadas não lembram quem começou. Só quem terminou.",
        "A honra é o luxo dos que ainda não sangraram.",
        "Cada cicatriz é um recibo da vida te cobrando.",
        "Quando o aço canta, os deuses se calam.",
        "Batalhar é conversar com a morte... em voz alta.",
        "Os fracos rezam. Os fortes empunham.",
        "A batalha é sincera — mata todos igualmente.",
        "A guerra não escolhe lados. Só corpos.",
        "Já vi homens valentes chorarem diante do som de um arco.",
        "A guerra transforma a coragem em moeda e o medo em lucro.",
        "As armas apenas obedecem. Quem trai é o coração.",
        "Os que lutam por glória morrem por vaidade.",
        "Não há vitória, apenas intervalos entre derrotas.",
        "O primeiro golpe é fácil. O último, raramente é seu.",
        "O sangue tem um som. Eu reconheço de longe.",
        "A coragem é apenas medo com boa postura.",
        "Nenhum aço é puro depois de matar.",
        "A guerra é o vício mais antigo da humanidade.",
        "As lâminas não dormem. Elas esperam.",
        "A paz é o maior inimigo do lucro.",
        "A batalha é uma arte. A sobrevivência, uma bênção rara.",
        "Os tolos lutam por honra. Os sábios lutam por ouro.",
        "O campo de batalha é o único lugar onde as mentiras morrem rápido.",
        "A cada golpe, o mundo esquece mais um nome.",
        "A guerra é um mercado, e eu sou o único vendedor feliz.",
        "Quando o sangue ferve, o raciocínio evapora.",
        "Não há música mais bela que o som do metal partindo carne.",
        "A coragem não protege de uma lâmina bem colocada.",
        "O medo move mais exércitos do que a glória.",
        "Os mortos são clientes que nunca reclamam.",
        "A guerra é generosa com quem sabe vender.",
        "Cada batalha é um contrato com a eternidade — e ela sempre cobra.",
        "Lutar é fácil. Esquecer é impossível.",
        "A vitória custa caro. A derrota custa tudo.",
        "O aço e o sangue são irmãos inseparáveis.",
        "Em Vangurd, até o vento corta.",
        "As espadas não julgam — apenas decidem quem sangra primeiro.",
        "O campo de batalha não tem eco. Só silêncio.",
        "As guerras terminam, mas o comércio... nunca.",
        "Todo combate é uma conversa entre destino e aço.",
        "A guerra é um poema que sempre rima com morte.",
        "Os vivos contam histórias. Os mortos apenas inspiram preços.",
        "A guerra começa com discursos e termina com gritos.",
        "Eu vendo as ferramentas, o resto é escolha sua.",
    ],

    "guilda": [
        "Guildas... alianças frágeis disfarçadas de irmandade.",
        "Onde há ouro, há uma guilda querendo dividir o lucro.",
        "As guildas prometem lealdade... até o primeiro saque.",
        "Já vendi lâminas a irmãos que se mataram em nome de suas bandeiras.",
        "A união é bela, até alguém contar o tesouro.",
        "Guildas? Chamaria de mercados com brasões.",
        "O poder coletivo é só um jeito mais elegante de explorar.",
        "Os líderes de guilda falam de honra... enquanto contam moedas.",
        "Vangurd já teve guildas demais. Hoje só restam túmulos com nomes pomposos.",
        "As guildas morrem do mesmo veneno que servem: ambição.",
        "Toda aliança nasce da desconfiança.",
        "As guildas não lutam por ideais — lutam por contratos.",
        "Um homem sozinho é previsível. Uma guilda... imprevisivelmente perigosa.",
        "Já vi mais traições em uma guilda do que em uma taverna.",
        "As guildas são famílias. Famílias cobram caro.",
        "As promessas de uma guilda valem menos que o ferro enferrujado.",
        "As guildas acreditam que podem controlar o caos. Ingenuidade cara.",
        "Onde há organização, há corrupção.",
        "Guildas são como lâminas: afiadas e perigosas de ambos os lados.",
        "A confiança é o primeiro recurso a acabar em uma guilda.",
        "Toda guilda começa com sonhos e termina em dívidas.",
        "A glória coletiva é o disfarce da cobiça individual.",
        "Vangurd já foi unida. Depois que o ouro chegou, a união sumiu.",
        "As guildas só duram enquanto houver inimigos — ou lucros.",
        "Um juramento de guilda vale menos que uma espada lascada.",
        "O maior inimigo de uma guilda é a própria sede de poder.",
        "Já vi líderes chorarem mais por ouro perdido do que por irmãos mortos.",
        "Guildas são espelhos de seus criadores: quebram fácil.",
        "A lealdade acaba quando o pagamento atrasa.",
        "Toda guilda acredita ser eterna. Nenhuma é.",
        "A força de uma guilda está no medo que inspira, não no brasão que ostenta.",
        "As guildas são templos do ego disfarçados de fraternidade.",
        "Um homem livre vale mais do que dez amarrados por promessas.",
        "A união é bela — até o ouro entrar na conversa.",
        "A paz entre guildas é apenas silêncio antes da punhalada.",
        "O brasão é apenas uma bandeira sobre uma pilha de ossos.",
        "As guildas de Vangurd aprenderam que a amizade é cara demais.",
        "Quem fala em nome da guilda raramente fala em nome da verdade.",
        "A ganância é o verdadeiro mestre de todas as guildas.",
        "Alguns chamam de cooperação, eu chamo de conspiração.",
        "Toda guilda tem um traidor — às vezes ele usa a coroa.",
        "A glória compartilhada é apenas vaidade repartida.",
        "As guildas não constroem o mundo. Elas o vendem.",
        "Já vi alianças nascerem com um brinde e morrerem com um golpe.",
        "Os contratos da guilda são escritos em sangue, não em tinta.",
        "A união é uma lâmina de dois gumes.",
        "As guildas são teias, e cada membro... uma presa.",
        "Quando o ouro fala, até os juramentos se calam.",
        "A guerra das guildas é eterna. Eu só vendo as armas.",
    ],
    "xingamento": [
        "Palavras ásperas não ferem como uma lâmina bem lançada.",
        "Cuidado com sua língua, viajante. Algumas lâminas escutam mais do que você pensa.",
        "O desprezo é barato, mas eu cobro caro por ele.",
        "Você fala com raiva. Eu vendi paciência há muito tempo.",
        "Chame-me de nomes, mas mantenha o ouro em mãos.",
        "Insultos não me afetam. Mas distrações podem custar sua vida.",
        "Você gagueja na raiva; eu gaguejo apenas com ferro.",
        "Xingar-me não muda a realidade, só a sua vergonha.",
        "A língua afiada quebra fácil… prefira uma espada.",
        "Palavras mal colocadas são como lâminas cegas: inúteis e perigosas.",
        "A raiva revela mais sobre você do que sobre mim.",
        "As maldições verbais não penetram minha couraça de aço.",
        "Cuidado: algumas palavras carregam intenções que você não imagina.",
        "Ofensas não pagam minhas mercadorias.",
        "A paciência é minha lâmina mais letal. Cuidado ao testá-la.",
        "Gritar não muda nada. E meu estoque não é infinito.",
        "Você fala muito. O aço fala mais.",
        "As palavras cortam, mas não tão profundamente quanto uma lâmina bem feita.",
        "Xingar alguém que vende armas afiadas é o mesmo que brincar com fogo.",
        "A cólera é um cliente pobre. O ouro, um cliente rico.",
        "Sua língua pode ser afiada, mas não o suficiente para mim.",
        "As palavras mal colocadas ecoam como gritos vazios na loja.",
        "O ferro não sente dor; mas ouve cada insulto.",
        "Você insulta, eu observo. O mercado decide.",
        "As palavras podem cortar, mas o aço finaliza.",
        "Gritos e raiva não compram nada. Apenas afastam clientes.",
        "As palavras são leves, mas o aço é pesado.",
        "Cuidado, viajante: até as palavras têm repercussões.",
        "Ofensas gratuitas nunca resultam em nada de bom.",
        "Xingar é um talento de tolos; negociar é um dom de poucos.",
        "Você acredita que suas palavras têm força? Experimente o aço.",
        "O rancor é frágil; o ferro, eterno.",
        "Não subestime o silêncio de um vendedor paciente.",
        "Suas ofensas são eco no vazio. Meu estoque, real.",
        "Falar alto não torna suas palavras mais verdadeiras.",
        "Insultar é uma arte mal dominada por muitos.",
        "Palavras duram segundos; uma lâmina bem lançada dura para sempre.",
        "Cuidado: algumas línguas cortam mais que espadas.",
        "O ferro não responde aos insultos, mas observa os indecisos.",
        "Xingar é fácil. Sobreviver, nem tanto.",
        "Sua língua é rápida, mas minha lâmina é mais.",
        "As palavras vazias ecoam, mas não me atingem.",
        "Gritar não muda o preço das lâminas.",
        "A arrogância fala alto, mas o aço fala primeiro.",
        "Você acredita que a cólera pesa? Experimente uma espada.",
        "Ofender não abre portas. Pagar, sim.",
        "As palavras que você escolhe não pesam nada aqui.",
        "O insulto é gratuito; o aço, não.",
        "Falar alto não muda o destino. Só incomoda o vendedor.",
        "A língua pode ferir, mas o aço decide.",
        "Xingamentos só afastam o cliente que paga menos.",
        "Não subestime o poder do silêncio — e do estoque afiado.",
    ],
    "ferreiro": [
        "O ferreiro domina o fogo; eu domino o destino que suas lâminas carregam.",
        "Ele molda o aço; eu determino quem empunha o poder da lâmina.",
        "As chamas do ferreiro revelam a forma; o comércio revela o valor.",
        "O calor do martelo não se compara ao peso de uma espada na mão certa.",
        "Já vi ferreiros chorar de cansaço; mas o aço nunca lamenta.",
        "A lâmina nasce do fogo; sua utilidade nasce da minha venda.",
        "Um bom ferreiro cria arte; um bom comerciante cria história.",
        "O ferreiro conhece o aço; eu conheço aqueles que o carregam.",
        "Algumas lâminas exigem cuidado, outras exigem coragem.",
        "O aço quente obedece ao martelo; o frio, ao dono da lâmina.",
        "O ferreiro dá forma, mas eu dou propósito.",
        "O cheiro do carvão é familiar; o cheiro do metal recém-forjado é irresistível.",
        "As mãos do ferreiro cansam, mas a lâmina nunca desiste.",
        "Cada espada tem segredos que só o comerciante descobre.",
        "O ferro se curva diante do fogo; o homem, diante do perigo.",
        "A forja é o ventre; a loja, o mundo que a lâmina vai conhecer.",
        "O ferreiro tem paciência; eu, precisão.",
        "Algumas lâminas precisam de ferreiro, outras de cliente audaz.",
        "O aço fala com o ferreiro; eu traduzo para quem entende a morte.",
        "As brasas brilham; o destino de quem empunha brilha mais.",
        "O ferreiro pode criar lâminas impecáveis; mas o uso correto é uma arte rara.",
        "O martelo molda metal; a sabedoria molda guerreros.",
        "A lâmina perfeita só encontra seu valor nas mãos certas.",
        "O ferreiro cria soldados de metal; eu os transformo em histórias.",
        "As faíscas do fogo refletem nos olhos do comerciante atento.",
        "O ferreiro conhece o calor; eu conheço a frieza de quem luta.",
        "Alguns ferreiros são mestres; poucos são artistas. Ainda menos, sobrevivem.",
        "O aço lembra o toque do martelo; eu lembro o toque do destino.",
        "A lâmina canta para o ferreiro; mas a música é ouvida por quem a compra.",
        "O ferreiro forja com força; eu vendo com visão.",
        "Algumas lâminas exigem sangue para provar seu valor.",
        "O ferro não mente; o ferreiro apenas segue ordens.",
        "O comerciante vê o mundo que a lâmina vai cortar.",
        "Cada golpe do martelo é uma promessa; cada venda, uma realização.",
        "O ferreiro vê a forma; eu vejo a função.",
        "O calor que derrete metal não se compara à pressão de um cliente esperto.",
        "Alguns ferreiros falam muito; o aço fala mais.",
        "O ferreiro trabalha para sobreviver; eu trabalho para entender.",
        "O martelo molda metal; a mente molda o futuro.",
        "O aço que brilha hoje, amanhã pode ser lenda ou lamento.",
        "O ferreiro cria potencia; eu ensino prudência.",
        "As mãos do ferreiro cansam; meus olhos nunca fecham.",
        "Cada espada carregada de ferro tem história; cada história carregada de ouro também.",
        "O martelo ecoa; minha voz é o silêncio que decide o preço.",
        "O calor da forja não amolece meu julgamento.",
        "O ferreiro ensina paciência; a lâmina ensina respeito.",
        "Alguns cortes exigem apenas força; outros, astúcia.",
        "O ferro é moldável; a coragem, não.",
        "O ferreiro tem talento; eu tenho visão.",
        "O aço obedece ao fogo; o mundo obedece a quem o domina.",
        "Cada lâmina que sai da forja espera pelo toque certo.",
        "O ferreiro é arte; o comerciante, estratégia.",
        "O martelo pode cantar; a lâmina decide quem ouve.",
        "O ferro precisa do calor; o guerreiro precisa da lâmina.",
        "O ferreiro é profeta do aço; eu sou o arauto do destino.",
        "As brasas são testemunhas; o comércio é juiz.",
        "O aço é eterno; o martelo, efêmero. Mas a escolha permanece.",
    ],
    "loja": [
        "Minha loja é um templo de aço e paciência.",
        "Cada prateleira guarda uma história de guerra e sobrevivência.",
        "Aqui, até o pó tem valor — é ouro em memória e ferro.",
        "O cliente que entra é um teste; o aço, a resposta.",
        "As lâminas que vendo carregam destino, não apenas metal.",
        "O silêncio da loja pesa mais que qualquer espada.",
        "Cada esquina desta loja tem olhos — ou melhor, lâminas.",
        "O ferro não mente; a disposição dos produtos também não.",
        "As sombras observam os passos de quem entra.",
        "Não vendo esperança; vendo oportunidade e perigo.",
        "Cada compra é uma escolha que ecoa mais que moedas.",
        "Meu estoque conhece mais batalhas que muitos guerreiros.",
        "A loja não fecha, apenas espera os corajosos e tolos.",
        "Alguns entram com medo; saem com o peso da decisão.",
        "O cheiro do metal frio mistura-se ao medo e à ambição.",
        "Aqui, os preços são honestos, mas o destino é imprevisível.",
        "As lâminas não se vendem sozinhas; escolhem seu portador.",
        "O chão da loja guarda mais histórias que o livro mais antigo.",
        "Cada espada tem uma assinatura, cada cliente uma intenção.",
        "Alguns entram em busca de glória, outros de destruição.",
        "O silêncio da loja é interrompido apenas pelo tilintar do metal.",
        "O aço espera, paciente, pelo toque certo.",
        "Quem olha demais, paga o preço da curiosidade.",
        "As prateleiras são testemunhas de escolhas irreversíveis.",
        "Não vendo armas, vendo decisões de sangue e suor.",
        "O cliente que hesita aprende rápido o valor da certeza.",
        "As sombras da loja parecem dançar entre as lâminas.",
        "Cada canto guarda segredos que o tempo jamais apagará.",
        "As lâminas brilham mais quando são desejadas com astúcia.",
        "A loja respira com quem entra, mas não se engana facilmente.",
        "O ouro fala alto, mas o aço decide quem sobrevive.",
        "As vendas são temporais; o impacto, eterno.",
        "Não há truques aqui, apenas escolhas e consequências.",
        "Cada porta que se abre revela mais do que mercadorias.",
        "O frio do aço contrasta com a ambição do cliente.",
        "Alguns retornam, outros se perdem antes de atravessar a porta.",
        "O cheiro do ferro lembra que a guerra está sempre próxima.",
        "Minha loja não julga; apenas observa e registra.",
        "As prateleiras contam histórias mais do que qualquer contador.",
        "O tilintar de uma lâmina anuncia decisões silenciosas.",
        "O cliente entra com desejo; sai com responsabilidade.",
        "A loja conhece os medos de cada comprador antes deles.",
        "Não vendo sonhos; vendo ferramentas para moldá-los.",
        "As lâminas esperam com paciência, o cliente, com ansiedade.",
        "Alguns pagam com ouro; outros, com ignorância.",
        "O aço brilha para quem sabe enxergar além do metal.",
        "Cada canto guarda tanto valor quanto risco.",
        "A loja é neutra, mas o destino não é.",
        "Quem compra aqui aprende rápido que escolhas têm peso.",
        "O silêncio fala mais alto que qualquer anúncio.",
        "Cada venda é um capítulo novo em histórias antigas.",
        "O cliente que observa demais percebe o valor real.",
        "Minha loja é só o início daquilo que o aço pode ensinar.",
        "Quem entra aqui nunca é o mesmo que sai.",
        "O comércio é uma arte; a lâmina, a sua musa.",
    ],
    "taverna":[
        "As histórias da taverna chegam a mim antes mesmo dos bêbados.",
        "Entre goles e gritos, vejo quem realmente precisa de uma lâmina.",
        "O cheiro de cerveja mistura-se ao medo e à ambição dos clientes.",
        "A taverna é palco de glórias efêmeras e memórias sangrentas.",
        "As risadas escondem mais perigos do que espadas à venda.",
        "Alguns entram para beber, outros para medir coragem.",
        "Os bêbados falam, mas o aço observa em silêncio.",
        "A taverna respira confusão, e eu registro cada movimento.",
        "Entre canecas e garrafas, planejam-se guerras e alianças.",
        "Os bêbados de hoje podem ser os heróis de amanhã… ou cadáveres.",
        "A música abafada não esconde as intenções dos presentes.",
        "O tilintar das canecas anuncia mais do que comemorações.",
        "Alguns clientes se perdem em bebidas, outros se encontram em aço.",
        "O riso alto é muitas vezes a máscara do desespero.",
        "Entre fumaça e cerveja, o destino se decide silencioso.",
        "O bêbado fala alto; a lâmina decide calar.",
        "As histórias contadas na taverna têm preço em suor e sangue.",
        "Entre copos e sussurros, o mundo muda sem perceber.",
        "O calor da taverna aquece, mas a verdade do aço corta.",
        "A confusão é constante, mas as lâminas permanecem observando.",
        "Os bêbados acreditam ser invencíveis; o aço não se engana.",
        "Cada conversa é um teste, cada escolha, um risco.",
        "A taverna é teatro; eu assisto de camarote.",
        "Entre gritos e brindes, surgem planos que o mundo esquecerá.",
        "Alguns bebem para esquecer; outros bebem para lembrar do medo.",
        "O tilintar das moedas se mistura ao tilintar do metal.",
        "Os bêbados não percebem que o destino está à venda.",
        "O silêncio entre as risadas é mais eloquente que os gritos.",
        "Cada briga é uma oportunidade, cada olhar uma advertência.",
        "A taverna guarda segredos que nem os mais corajosos descobrem.",
        "As risadas podem enganar, mas o aço não.",
        "Entre histórias exageradas, reconheço quem busca verdade.",
        "O calor da bebida não apaga o frio das lâminas.",
        "Os bêbados falam demais; o mercado escuta mais.",
        "Cada mesa tem um drama, cada copo um mistério.",
        "A taverna é cheia de vida, mas também de sombras.",
        "Alguns entram como clientes, saem como lembranças amargas.",
        "A confusão temporária revela intenções permanentes.",
        "Entre cantos e cânticos, a ambição se move sorrateira.",
        "As brigas são testes; quem sobrevive, pode comprar minha lâmina.",
        "O bêbado que ri alto provavelmente chora em silêncio depois.",
        "A taverna é o microcosmo do mundo; eu sou o observador.",
        "Entre o álcool e o medo, surgem os verdadeiros corajosos.",
        "O tilintar das moedas e das lâminas marca o ritmo da noite.",
        "As histórias contadas aqui serão esquecidas, mas os erros permanecem.",
        "Alguns buscam diversão; outros buscam redenção em aço.",
        "O calor da bebida engana; a lâmina ensina.",
        "Os bêbados são passageiros; o aço, eterno.",
        "Entre gritos e risadas, a verdade se esconde nas sombras.",
        "A taverna é um campo de treino para aqueles que desejam sobreviver.",
        "Os excessos de hoje podem custar caro amanhã.",
        "Cada brinde é um risco, cada olhar, uma decisão.",
        "Entre a fumaça e o barulho, o aço espera pacientemente.",
        "Quem entra acreditando em sorte, sairá acreditando em escolhas.",
    ],
    "vilas": [
        "Vangurd é apenas uma pedra no mapa de Eldora, mas suas lâminas são lembradas em todas as vilas.",
        "Cada vila tem sua história; cada lâmina que vendo, seu impacto.",
        "As vilas crescem, caem e sangram; meu comércio permanece.",
        "Alguns vilarejos esquecem seus heróis; eu lembro de quem carrega minhas lâminas.",
        "O povo das vilas pode ignorar a guerra, mas não o aço.",
        "Em cada vila, há quem sonha e quem teme; minhas lâminas escolhem os corajosos.",
        "Algumas vilas prosperam com trabalho; outras, com sangue e metal.",
        "As pragas passam, mas o aço permanece.",
        "O mercado das vilas é instável, mas o valor do aço é constante.",
        "Cada vila tem suas leis; minha lâmina decide quem as desafia.",
        "O povo das vilas compra esperança ou medo — sempre com preço.",
        "Alguns vilarejos ignoram os perigos; minhas lâminas não.",
        "Entre campos e casas, meus produtos encontram seu caminho.",
        "Cada vila tem sua reputação; cada lâmina, sua lenda.",
        "O sucesso de uma vila depende de coragem, não de sorte.",
        "Alguns vilarejos são esquecidos; eu nunca esqueço os que precisam de aço.",
        "O vento traz rumores das vilas; minhas lâminas carregam a realidade.",
        "Cada vila tem seu ritmo, mas o aço dita seu próprio compasso.",
        "Alguns heróis nascem nas vilas; outros, nas sombras de Vangurd.",
        "As vilas podem ser pequenas, mas cada decisão ecoa por Eldora.",
        "O comerciante conhece os caminhos das vilas como poucos conhecem seus próprios quintais.",
        "A história de uma vila muitas vezes depende de quem possui a lâmina certa.",
        "Algumas vilas oferecem ouro; outras, histórias de coragem.",
        "O aço nunca se engana; o povo das vilas, às vezes sim.",
        "Entre casas e praças, observo quem merece o verdadeiro poder.",
        "O destino de uma vila pode mudar com uma lâmina bem entregue.",
        "Cada vila é um tabuleiro; minhas lâminas, peças decisivas.",
        "Algumas vilas esquecem seus filhos; eu não esqueço meus clientes.",
        "O comércio corre pelas vilas como um rio invisível, mas certeiro.",
        "Cada aldeão tem suas ambições; cada lâmina, sua utilidade.",
        "As vilas contam segredos antigos; o aço revela novos.",
        "Algumas vilas sangram; outras brilham, mas todas são influenciadas pelo comércio.",
        "O vento do norte traz notícias; minhas lâminas carregam consequências.",
        "Alguns vilarejos são pacíficos; outros, terrenos férteis para batalhas.",
        "O sucesso de uma vila é efêmero; o peso de uma lâmina, eterno.",
        "Cada vila tem seu herói; algumas, seu carrasco.",
        "Entre estradas de terra e mercados ruidosos, observo quem se destaca.",
        "As vilas são espelhos do mundo; o aço, o reflexo da verdade.",
        "Alguns entram nas vilas com medo; saem armados de coragem.",
        "O comércio conecta vilas, mas cada decisão permanece individual.",
        "Cada vila guarda histórias de vitória e derrota; minhas lâminas testemunham ambas.",
        "Alguns vilarejos florescem; outros murcham, mas o aço sempre resiste.",
        "As vilas podem subestimar o perigo; minhas lâminas não.",
        "Cada vila tem seu segredo; cada lâmina, sua chave.",
        "Entre o cotidiano e o inesperado, o comerciante observa e decide.",
        "Algumas vilas são pequenas; mas cada vida conta, cada lâmina pesa.",
        "O vento da manhã revela quem está pronto; a lâmina confirma.",
        "O aço que entra em uma vila deixa marcas que duram mais que pedras.",
        "Cada estrada que leva a uma vila é também um caminho de oportunidades.",
        "As vilas podem ser esquecidas pelo tempo; eu não esqueço seus corajosos.",
        "Algumas vilas brilham à luz do sol; outras, sob a sombra das lâminas.",
        "O destino das vilas é selado pelas escolhas e pelo aço que carregam.",
    ],
    "clima": [
        "Chuva ou sol, o aço permanece fiel, diferente dos homens.",
        "O vento anuncia tempestades; minhas lâminas permanecem calmas.",
        "O céu pode se abrir em tormenta; meu comércio não vacila.",
        "A neblina esconde caminhos; mas o aço revela verdades.",
        "O frio penetra os ossos, mas não a precisão de uma lâmina.",
        "O calor cega os fracos; o ferro continua inalterado.",
        "A chuva molha roupas, mas o destino permanece seco e afiado.",
        "Tempestades são apenas testes; o aço observa silencioso.",
        "O sol aquece a pele; o aço aquece o respeito.",
        "O vento uiva, mas não assusta aqueles que conhecem o perigo.",
        "O gelo quebra galhos; minhas lâminas não se quebram tão facilmente.",
        "A chuva cai, mas minhas decisões permanecem firmes.",
        "O céu escuro esconde traições; o aço revela intenções.",
        "O calor do dia não apaga o frio que carrego no olhar.",
        "O trovão anuncia caos; minhas lâminas anunciam destino.",
        "A tempestade testa coragem; o aço testa verdade.",
        "A brisa suave engana; minhas lâminas não se enganam.",
        "O orvalho da manhã não diminui o peso do perigo.",
        "O sol se põe, mas minha vigilância permanece.",
        "O nevoeiro oculta inimigos; o aço os expõe.",
        "O vento sopra rumores; minhas lâminas ouvem certezas.",
        "Chuva, sol, neblina… o tempo muda, o ferro não.",
        "O trovão ecoa histórias; o aço cria finais.",
        "O calor do deserto ensina paciência; o aço ensina respeito.",
        "O gelo corta; minhas lâminas cortam destinos.",
        "O vento do norte traz notícias; minhas lâminas trazem consequências.",
        "O céu em fúria reflete a guerra por vir.",
        "A chuva insiste, mas as escolhas permanecem secas e afiadas.",
        "O frio aproxima os fracos; separa os fortes.",
        "A tempestade anuncia caos, e o aço anuncia ordem.",
        "O sol brilha para todos, mas apenas alguns veem o valor do aço.",
        "O nevoeiro esconde intenções, o aço revela verdades.",
        "O calor do verão não derrete a precisão de uma lâmina.",
        "O vento sussurra segredos; minhas lâminas respondem com cortes.",
        "O céu escuro não muda o aço frio em minha mão.",
        "A chuva cai como aviso; a lâmina como sentença.",
        "O gelo endurece caminhos; o ferro endurece destinos.",
        "O vento muda de direção, mas minha atenção não vacila.",
        "O calor da forja é menor que o calor da ambição humana.",
        "O trovão ecoa decisões; minhas lâminas ecoam consequências.",
        "A neblina mascara erros; o aço não perdoa.",
        "O sol desponta; o aço observa, impassível.",
        "A tempestade chega; o comércio continua.",
        "O frio aproxima a morte; o ferro aproxima a justiça.",
        "O vento levanta poeira; minhas lâminas levantam respeito.",
        "Chuva, neve, sol… o clima muda, mas minhas lâminas permanecem.",
        "O trovão anuncia perigo; minha lâmina anuncia resolução.",
        "O céu ameaça, mas o aço oferece certeza.",
        "O vento traz rumores; minha lâmina traz a verdade.",
        "A chuva lava a cidade; o aço lava dúvidas.",
        "O frio penetra a pele, mas não a decisão de quem empunha o ferro.",
        "A tempestade testa todos; o aço seleciona apenas os dignos.",
    ],
    "ajuda": [
        "Posso ajudá-lo com uma espada, mas não com a coragem que precisa para usá-la.",
        "A ajuda que ofereço tem preço, e nem todos conseguem pagá-lo.",
        "Não dou chances a imprudentes; ajudo aqueles que entendem o perigo.",
        "Uma lâmina pode salvar, mas a estratégia salva mais.",
        "Ajudar é uma arte; poucos dominam sem custo.",
        "O caminho da ajuda é estreito e cheio de escolhas difíceis.",
        "Posso mostrar como o aço corta, mas não como enfrentar o medo.",
        "Ajudar não significa intervir; significa fornecer as ferramentas certas.",
        "A lâmina em sua mão não garante vitória, apenas oportunidade.",
        "Meu auxílio é seletivo; cada escolha ecoa pelo futuro.",
        "Posso guiar seus passos, mas não seus pensamentos.",
        "A ajuda que ofereço depende da inteligência de quem aceita.",
        "Cada instrução é um teste; cada conselho, uma lâmina invisível.",
        "Ofereço ferramentas, não milagres.",
        "Ajudar é plantar sementes; a colheita depende do cultivador.",
        "Não protejo os tolos; apenas ensino-os a se proteger.",
        "O auxílio vem para quem merece e para quem sabe ouvir.",
        "Uma lâmina na mão certa é ajuda; na errada, destruição.",
        "Minhas instruções pesam mais que o ouro que você carrega.",
        "Ajudar é mais mostrar o caminho do que andar por ele.",
        "Posso fortalecer suas chances, mas não suas fraquezas.",
        "Cada conselho é uma lâmina disfarçada, pronta para cortar o desespero.",
        "Não existe ajuda sem responsabilidade.",
        "Meu auxílio é pontual; minha paciência, infinita para quem merece.",
        "Ensinar a usar uma espada é mais valioso que entregar a espada.",
        "Ajudar exige percepção; nem todos a possuem.",
        "Uma mão estendida é inútil se não houver coragem para agarrá-la.",
        "O aço pode guiar, mas a mente decide o sucesso.",
        "O auxílio chega, mas a escolha final é sempre sua.",
        "A ajuda é uma lâmina dupla: protege ou castiga.",
        "Posso abrir portas, mas você deve atravessá-las.",
        "Ajudar não é salvar; é preparar para enfrentar.",
        "Minhas instruções são afiadas; siga-as com atenção.",
        "O auxílio que ofereço é estratégico, não sentimental.",
        "Ensinar a lutar é mais que oferecer proteção; é ensinar liberdade.",
        "Ajudar é plantar sabedoria, colher experiência.",
        "Minhas ferramentas salvam; minha orientação evita erros.",
        "O apoio é dado a quem demonstra inteligência e coragem.",
        "Ajudar não elimina riscos; apenas maximiza oportunidades.",
        "Uma lâmina bem entregue vale mais que palavras inúteis.",
        "O auxílio que dou testa caráter antes de habilidade.",
        "Posso mostrar o caminho certo, mas não posso andar por você.",
        "A ajuda que ofereço vem com compreensão do perigo.",
        "Minha orientação corta dúvidas e revela caminhos.",
        "Posso ensinar técnicas, mas não posso garantir coragem.",
        "Ajudar é um investimento; nem todos valem o retorno.",
        "Cada instrução é um mapa; cada decisão, uma viagem.",
        "Ofereço estratégias, não atalhos.",
        "Ajudar exige confiança e respeito pelo processo.",
        "A lâmina em mãos experientes é auxílio; em mãos fracas, desastre.",
        "Minha ajuda é medida; cada passo precisa ser calculado.",
        "Não é compaixão que guia minha ajuda, mas sabedoria.",
        "Ajudar é compartilhar poder, não doar ilusões.",
        "Cada conselho é um fio que conecta intenção e ação.",
    ],
    "classes": [
        "Cavaleiros, magos, ladrões… todos buscam poder, mas poucos entendem o preço.",
        "Cada classe traz habilidades únicas, mas também responsabilidades ocultas.",
        "O bruxo domina a magia; o cavaleiro, o aço; o comerciante, o destino.",
        "Alguns nascem para liderar, outros para servir, e poucos para sobreviver.",
        "Cada classe tem sua força; cada escolha seu risco.",
        "O guerreiro busca glória, o mago, conhecimento; e eu observo quem usa melhor.",
        "O ladrão sabe aproveitar falhas; o paladino, criar oportunidades.",
        "A classe não garante vitória, apenas define possibilidades.",
        "Alguns confundem classe com poder; outros entendem seu verdadeiro valor.",
        "Cada habilidade é uma lâmina invisível, pronta para cortar o destino.",
        "O mago aprende a controlar o fogo; o guerreiro, a controlar a própria morte.",
        "Alguns guerreiros são fortes, mas sem estratégia, nada valem.",
        "Cada classe é uma ferramenta; quem as domina, molda a história.",
        "O arqueiro mira longe, mas seus erros ecoam próximos.",
        "O clérigo cura corpos, mas nem sempre almas.",
        "Alguns ladrões são silenciosos; outros, silenciosamente mortais.",
        "A classe define o estilo, mas não a coragem.",
        "O mago prepara feitiços; o guerreiro prepara planos; eu preparo oportunidades.",
        "Cada classe tem sua rotina; cada ação, sua consequência.",
        "O bárbaro briga com fúria; o estrategista briga com mente.",
        "O assassino escolhe alvo; o paladino escolhe justiça; eu observo ambos.",
        "A classe revela habilidades, mas esconde intenções.",
        "Cada cavaleiro tem honra; cada mercenário tem preço.",
        "O guerreiro levanta armas; o comerciante levanta histórias.",
        "O mago sonha com mundos; o ladrão os cria e destrói.",
        "Alguns heróis esquecem a disciplina da classe; outros, a aprendem cedo.",
        "Cada classe tem pontos fortes; cada falha, um aviso.",
        "O arqueiro espera pacientemente; o espadachim ataca imediatamente.",
        "O clérigo ora, mas não garante resultados.",
        "O guerreiro aprende força; o mago aprende paciência; o comerciante aprende a esperar.",
        "Cada habilidade é um teste; cada decisão, uma lâmina.",
        "O bárbaro sente o campo; o estrategista sente a batalha antes de começar.",
        "Alguns se perdem nas classes; outros se encontram.",
        "O ladrão observa detalhes que o guerreiro ignora.",
        "O paladino protege, mas às vezes impede o progresso.",
        "Cada classe ensina lições; cada falha ensina mais ainda.",
        "O mago depende do conhecimento; o guerreiro, da disciplina.",
        "O comerciante entende todas as classes sem pertencer a nenhuma.",
        "Algumas classes brilham; outras apenas sobrevivem.",
        "O arqueiro confia na mira; o guerreiro confia no coração.",
        "O clérigo cura feridas; o aço cria feridas que importam.",
        "Cada classe tem potencial, mas o uso define o legado.",
        "O ladrão aproveita a fraqueza; o comerciante aproveita o momento.",
        "O guerreiro é direto; o mago, indireto; e o destino, inevitável.",
        "Alguns heróis ignoram fraquezas; outros as exploram.",
        "Cada classe é uma história; cada ação, um capítulo.",
        "O espadachim desafia; o estrategista observa; eu decido.",
        "O bárbaro ruge, o clérigo ora, e o comerciante calcula.",
        "Cada classe tem sua glória; cada erro, uma lembrança eterna.",
        "O mago prevê; o guerreiro reage; o comerciante manipula.",
        "As classes não são iguais, mas todas dependem da mente que as comanda.",
        "O destino não escolhe classe; apenas testa aqueles que ousam agir.",
    ],
    "economia": [
        "O ouro fala mais alto que qualquer espada, mas a lâmina decide quem escuta.",
        "Cada moeda tem história; cada transação, destino.",
        "A economia não é sobre riqueza, mas sobre sobrevivência e poder.",
        "Alguns acumulam ouro; outros, experiência. Ambos têm valor.",
        "O preço das coisas é determinado pelo risco de consegui-las.",
        "O comércio ensina mais que a batalha; o lucro pesa mais que o sangue.",
        "A economia não dorme, mesmo quando as cidades fecham suas portas.",
        "Cada investimento é uma lâmina pronta para cortar erros.",
        "O ouro pode corromper; o conhecimento corrompe menos.",
        "A moeda é efêmera; as decisões financeiras, eternas.",
        "Alguns vendem por ouro; outros vendem a oportunidade.",
        "A economia observa quem é astuto, quem é ganancioso e quem é imprudente.",
        "Cada transação é um teste; cada falha, uma lição.",
        "O comércio move cidades; o aço decide quem sobrevive nelas.",
        "O preço das armas reflete mais que metal; reflete estratégia.",
        "Alguns ganham riqueza; poucos ganham respeito.",
        "O ouro é apenas ferramenta; a inteligência, arma real.",
        "Cada mercado tem seu pulso; quem o sente, prospera.",
        "A economia é tão cruel quanto a batalha; prepare-se.",
        "Alguns pagam ouro; outros pagam com vida.",
        "O comerciante não escolhe vítima; escolhe oportunidade.",
        "O lucro é passageiro, mas o conhecimento financeiro é duradouro.",
        "Cada oferta tem um risco oculto, cada venda, uma consequência.",
        "A economia não perdoa os desatentos.",
        "O dinheiro fala, mas quem entende suas entrelinhas, comanda.",
        "O valor não está na moeda, mas em quem a usa sabiamente.",
        "Alguns acumulam riqueza; outros, sabedoria. Ambas podem comprar sobrevivência.",
        "O comércio observa o mundo; cada transação revela intenções.",
        "O preço certo é tão mortal quanto qualquer lâmina.",
        "O mercado não tem compaixão; apenas exige atenção e astúcia.",
        "Cada investimento pode abrir portas ou criar armadilhas.",
        "O ouro pode ser escasso; a astúcia, sempre abundante.",
        "A economia é a batalha silenciosa que define o destino das vilas.",
        "Alguns medem riqueza; outros medem poder. O comerciante mede ambos.",
        "O mercado é um jogo de sombras; o lucro é a luz que poucos veem.",
        "Cada compra tem custo; cada falha tem consequência.",
        "O ouro não compra coragem; compra oportunidade de provar força.",
        "Alguns vendem por necessidade; outros, por ambição.",
        "O comerciante não julga; ele calcula.",
        "A riqueza é passageira; o entendimento da economia é eterno.",
        "Cada moeda conta, cada falha pesa.",
        "O mercado observa o fraco, o esperto e o imprudente com a mesma indiferença.",
        "Alguns buscam lucro; outros buscam controle. Ambos são perigosos.",
        "O comércio é a arte de transformar recursos em poder.",
        "O preço das armas nem sempre é em ouro; às vezes, em honra ou vida.",
        "A economia recompensa aqueles que entendem o tempo, a oferta e o risco.",
        "O comerciante domina a moeda; o aço domina o destino.",
        "Alguns mercados prosperam; outros quebram. O comerciante sobrevive a ambos.",
        "Cada transação é uma lição; cada falha, uma memória.",
        "O ouro brilha; a astúcia brilha mais.",
        "A economia ensina lições que a batalha não pode oferecer.",
        "Quem ignora o mercado, paga com sangue e suor.",
        "O comércio é silencioso, mas seus efeitos ecoam por toda Eldora.",
        "Cada moeda movida muda destinos invisíveis.",
    ],
    "npcs": [
        "Alguns moradores observam em silêncio, escondendo mais do que revelam.",
        "Entre comerciantes e aldeões, cada gesto conta uma história.",
        "Alguns homens falam demais; outros apenas registram em silêncio.",
        "As pessoas seguem rotinas, mas há intenções que escapam aos olhos comuns.",
        "Alguns habitantes guardam segredos valiosos, outros apenas barulho.",
        "Entre ruas e praças, o destino se move pelas mãos invisíveis de muitos.",
        "Alguns conhecem atalhos e passagens secretas; outros mal sabem o caminho.",
        "A aparência não revela o poder ou a ambição de quem você encontra.",
        "Alguns moradores ajudam de bom grado; outros por interesse.",
        "Cada conversa é uma pista disfarçada em palavras comuns.",
        "Alguns trabalham duro; outros observam e aproveitam oportunidades.",
        "Entre casas e mercados, histórias se entrelaçam sem aviso.",
        "Alguns vigiam você mais do que qualquer inimigo declarado.",
        "O silêncio de alguns fala mais alto que os gritos de outros.",
        "Alguns homens carregam conhecimento antigo; outros espalham mentiras.",
        "Entre aliados e rivais, intenções se revelam lentamente.",
        "Alguns tentam impressionar; outros manipulam em sombras.",
        "A lealdade é rara; a traição, previsível.",
        "Alguns lembram acontecimentos passados; outros esquecem por conveniência.",
        "Entre risadas e cumprimentos, observadores registram cada detalhe.",
        "Alguns compartilham segredos; outros apenas os escondem.",
        "As ações de cada pessoa podem alterar destinos silenciosamente.",
        "Alguns são corajosos; outros sobrevivem apenas por instinto.",
        "Entre mercadores e moradores, alianças se formam e se desfazem.",
        "Alguns aprendem rápido; outros tropeçam nas próprias intenções.",
        "O comportamento revela mais do que qualquer palavra.",
        "Alguns confundem bondade com ingenuidade; outros a exploram.",
        "Entre encontros casuais, há sempre algo em jogo.",
        "Alguns guardam tesouros, outros guardam conhecimento.",
        "Cada rosto tem histórias, desejos e segredos escondidos.",
        "Alguns ensinam sem perceber; outros aprendem em silêncio.",
        "O destino é moldado por aqueles que observam mais do que falam.",
        "Alguns ajudam; outros atrapalham. Poucos permanecem neutros.",
        "Entre aldeões e comerciantes, o equilíbrio muda a cada escolha.",
        "Alguns esquecem passado; outros o usam como arma.",
        "O olhar de alguns pesa mais que qualquer espada.",
        "Alguns confundem interesse com amizade; outros, silêncio com desprezo.",
        "Entre casas e becos, decisões invisíveis definem o futuro.",
        "Alguns agem por medo; outros por ambição.",
        "O mundo observa aqueles que menos esperam.",
        "Alguns moradores influenciam destinos sem jamais perceber.",
        "Entre aliados e adversários, intenções se revelam aos atentos.",
        "Alguns escondem coragem; outros exibem fraqueza.",
        "O passado de muitos é um guia silencioso para quem observa.",
        "Alguns trazem respostas; outros apenas mais perguntas.",
        "Entre rumores e histórias, a verdade se revela de forma sutil.",
        "Alguns oferecem ajuda, outros criam armadilhas disfarçadas.",
        "O que é dito é apenas parte do que realmente acontece.",
        "Alguns aprendem rápido; outros permanecem presos em erros antigos.",
        "Entre sussurros e olhares, decisões são tomadas sem alarde.",
        "Alguns são lembrados; outros esquecidos, mas nem todos os esquecidos estão inofensivos.",
        "O mundo observa e reage, e nem sempre você percebe quem puxa as cordas.",
        "Alguns atuam como peças comuns; outros são protagonistas silenciosos.",
    ],
    "elogios": [
        "Sua coragem é notável, digna dos livros que poucos ousam ler.",
        "A precisão em suas ações revela mais do que anos de treino; revela essência.",
        "Sua astúcia é uma lâmina afiada, capaz de cortar qualquer dúvida.",
        "O respeito que inspira é mais valioso que qualquer ouro acumulado.",
        "Sua determinação brilha mesmo nas trevas mais densas.",
        "A forma como enfrenta o perigo é digna de lendas esquecidas.",
        "Seu olhar revela inteligência e coragem em iguais proporções.",
        "A habilidade que demonstra é mais que talento; é arte refinada.",
        "O modo como age em silêncio é prova de grande sabedoria.",
        "Sua presença impõe ordem mesmo em caos absoluto.",
        "A paciência que possui é superior à força bruta de muitos.",
        "Seu julgamento é certeiro, como lâmina que nunca erra o alvo.",
        "O equilíbrio entre coragem e cautela é digno de mestres antigos.",
        "Sua estratégia revela mente capaz de manipular o destino.",
        "A confiança que inspira transforma aliados em heróis.",
        "Sua persistência ultrapassa limites que poucos ousam testar.",
        "O modo como analisa cada situação é admirável e preciso.",
        "Sua liderança surge não pela força, mas pelo respeito conquistado.",
        "A sagacidade que demonstra supera muitos anos de experiência.",
        "Sua coragem não é apenas evidente; é contagiante.",
        "O domínio de suas habilidades revela dedicação extrema.",
        "Sua visão estratégica antecipa movimentos que outros ignoram.",
        "A maneira como age revela confiança e conhecimento profundo.",
        "Seu discernimento corta ilusões como lâmina afiada.",
        "A precisão de seus gestos mostra controle absoluto.",
        "Sua bravura não é exibida; é silenciosa e mortal.",
        "O modo como supera obstáculos revela verdadeira força interior.",
        "Sua intuição é aguçada, como se o futuro falasse através de você.",
        "O respeito que merece não é imposto; é conquistado.",
        "Sua habilidade em resolver conflitos é tão mortal quanto seu aço.",
        "O modo como conduz situações complexas é exemplar.",
        "Sua determinação desafia o tempo e o perigo.",
        "A sabedoria que possui é rara, como relíquias esquecidas.",
        "Seu poder inspira aliados e intimida adversários.",
        "A forma como enfrenta inimigos é digna de epopéias.",
        "Sua coragem não conhece limites; é inabalável e contagiante.",
        "O modo como observa e age revela inteligência suprema.",
        "Sua força de vontade corta barreiras mais firmes que qualquer ferro.",
        "A determinação que demonstra transforma desafios em vitórias.",
        "Sua habilidade de leitura do ambiente é quase profética.",
        "O modo como inspira confiança é digno de líderes lendários.",
        "Sua calma diante do caos é mais letal que qualquer ataque.",
        "A forma como toma decisões demonstra grandeza rara.",
        "Sua persistência transforma adversidade em oportunidade.",
        "O respeito que evoca é conquistado com cada ação certeira.",
        "Sua capacidade de adaptação é impressionante e mortal.",
        "O modo como enfrenta desafios revela verdadeira essência de guerreiro.",
        "Sua presença transforma ambiente, impondo ordem e foco.",
        "A sabedoria que emana é um farol para aqueles ao redor.",
        "Sua astúcia supera armadilhas e estratégias inimigas.",
        "O modo como protege aliados é prova de coragem e inteligência.",
        "Sua determinação é silenciosa, mas inquebrável.",
        "A força que demonstra não é apenas física, mas mental e estratégica.",
        "Sua visão do combate e da vida é digna de heróis imortais.",
    ],
    "pergunta estado": [
        "Sigo firme, como aço temperado, pronto para qualquer desafio.",
        "Meu espírito está alerta, e minha lâmina preparada.",
        "Estou em plena forma, apesar das sombras que rondam Eldora.",
        "A batalha me fortalece; cada cicatriz conta história.",
        "Sigo vigilante, observando cada passo ao meu redor.",
        "Minha mente está clara, pronta para decisões difíceis.",
        "Estou pronto para o que vier, seja aço ou trevas.",
        "O corpo aguenta, a mente não cede; sigo firme.",
        "Sigo atento, cada som é um aviso e cada sombra, um segredo.",
        "A força me acompanha, mas a sabedoria me guia.",
        "O coração pulsa com determinação, mesmo diante do caos.",
        "Sigo preparado, mantendo o foco em cada movimento.",
        "Minha lâmina brilha, mas minha mente brilha mais.",
        "Estou alerta, percebendo até o menor detalhe ao redor.",
        "O sangue corre, mas a mente permanece fria e calculista.",
        "Sigo saudável e vigilante, como quem nunca se rende.",
        "O corpo resiste, o espírito domina; sigo equilibrado.",
        "Estou pronto para enfrentar perigos e desafios ocultos.",
        "Sigo firme, mantendo cada pensamento em prontidão.",
        "Minha energia se mantém, e minha atenção nunca falha.",
        "Estou consciente de cada passo e preparado para reagir.",
        "Sigo forte, a mente afiada e o coração destemido.",
        "O estado é sólido; nada ameaça minha determinação.",
        "Sigo incólume, apesar do peso do mundo sobre os ombros.",
        "Minha força interior é firme; meu corpo acompanha.",
        "Estou pronto para decisões rápidas e ações decisivas.",
        "Sigo alerta, atento a traições e armadilhas invisíveis.",
        "O espírito não vacila; a mente continua precisa.",
        "Sigo firme, cada músculo e pensamento alinhados ao propósito.",
        "Minha energia é constante, e meu foco, inabalável.",
        "Estou preparado para qualquer desafio que Eldora imponha.",
        "Sigo equilibrado, corpo e mente trabalhando em perfeita harmonia.",
        "O estado é estável; nada ameaça meu controle sobre a situação.",
        "Sigo pronto, vigilante e consciente de cada possibilidade.",
        "Minha mente afiada e o corpo resistente caminham juntos.",
        "Estou em posição, pronto para agir com precisão e sabedoria.",
        "Sigo firme, a atenção plena e a coragem intacta.",
        "Minha força persiste, e minha determinação não cede.",
        "Estou alerta, cada sentido desperto para o que se aproxima.",
        "Sigo em paz comigo mesmo, mas preparado para qualquer conflito.",
        "O corpo aguenta; a mente domina; sigo imperturbável.",
        "Estou consciente e atento, pronto para enfrentar o inesperado.",
        "Sigo vigilante, percebendo até o menor movimento ao redor.",
        "A mente e o corpo estão sincronizados, prontos para ação.",
        "Sigo firme, mesmo quando o mundo parece conspirar contra mim.",
        "O estado é equilibrado, e minha resolução permanece inquebrável.",
        "Sigo preparado, mantendo cada habilidade e estratégia afiadas.",
        "Minha atenção não vacila; cada perigo é antecipado.",
        "Estou em plena forma, pronto para qualquer desafio que surja.",
        "Sigo firme, mente clara, corpo resistente, espírito indomável.",
        "Minha determinação é sólida, pronta para qualquer provação.",
        "Sigo alerta, cada passo calculado, cada gesto medido.",
    ],
    "despedida": [
        "Vá com cuidado, pois nem toda sombra deseja sua segurança.",
        "Parta agora, e que seus passos sejam guiados pela sorte.",
        "Adeus, aventureiro, que os ventos de Eldora te protejam.",
        "Siga seu caminho, mas lembre-se: o mundo observa cada escolha.",
        "Que sua lâmina permaneça afiada e seu espírito inquebrável.",
        "Vá, mas carregue consigo a atenção e a astúcia.",
        "Parta em segurança, e que as trevas nunca sejam seu abrigo.",
        "Adeus, que seus inimigos sejam enganados e seus aliados leais.",
        "Siga adiante, mas não subestime o perigo que espreita.",
        "Vá com cuidado, pois cada esquina pode esconder armadilhas.",
        "Parta agora, e que sua coragem não vacile diante do desafio.",
        "Adeus, que o caminho se revele mais claro que a sombra.",
        "Siga seu rumo, mas jamais perca a vigilância.",
        "Vá, e que a experiência guie seus passos incertos.",
        "Parta, mantendo sua mente afiada e seu coração firme.",
        "Adeus, aventureiro, que sua jornada seja marcada por glórias.",
        "Siga em segurança, mas lembre-se: cada escolha tem consequência.",
        "Vá, e que a sorte caminhe ao seu lado, ainda que silenciosa.",
        "Parta agora, e que sua determinação nunca fraqueje.",
        "Adeus, que seus caminhos cruzem aliados, não inimigos.",
        "Siga em frente, e que a astúcia seja seu maior aliado.",
        "Vá, mas nunca ignore os sinais que Eldora sussurra.",
        "Parta, mantendo a calma mesmo diante das tempestades.",
        "Adeus, que o aço e a sabedoria estejam sempre com você.",
        "Siga seu caminho, mas não deixe de aprender com cada passo.",
        "Vá, e que a coragem ilumine mesmo a noite mais escura.",
        "Parta agora, mantendo vigilância sobre cada sombra.",
        "Adeus, que cada desafio seja superado com inteligência e força.",
        "Siga adiante, mas nunca perca a atenção aos detalhes.",
        "Vá, e que sua jornada seja marcada por escolhas certeiras.",
        "Parta, com a mente alerta e o coração preparado.",
        "Adeus, que a experiência seja seu guia mais confiável.",
        "Siga seu rumo, e que a sorte favoreça suas decisões.",
        "Vá com cuidado, e que cada passo seja dado com estratégia.",
        "Parta agora, e que a coragem nunca abandone sua alma.",
        "Adeus, aventureiro, que cada batalha traga aprendizado.",
        "Siga em frente, mas nunca subestime os riscos ocultos.",
        "Vá, e que seu caminho seja iluminado pela prudência.",
        "Parta, mantendo firmeza diante da incerteza.",
        "Adeus, que sua jornada seja longa, mas segura.",
        "Siga seu caminho, e que os perigos se transformem em lições.",
        "Vá, mas carregue consigo a atenção aos detalhes e a coragem.",
        "Parta agora, e que a vitória seja seu destino, não acaso.",
        "Adeus, que cada encontro seja uma oportunidade de crescimento.",
        "Siga adiante, mantendo cada passo calculado e seguro.",
        "Vá, e que a astúcia e a força sejam inseparáveis.",
        "Parta, mantendo o foco e a determinação em cada ação.",
        "Adeus, aventureiro, que sua jornada seja épica e segura.",
        "Siga em frente, mas jamais se torne imprudente.",
        "Vá, e que Eldora recompense seu esforço e sabedoria.",
        "Parta agora, e que o perigo seja sempre antecipado.",
        "Adeus, que a experiência e a coragem caminhem juntas com você.",
    ],
}

respostas_comerciante_rimvark = {
    "saudacao": ["Ora, ora... um novo freguês? Que delícia!", "Entre e veja o que há de bom, mas traga ouro!"],
    "batalha": ["Batalha? Que ótimo! Quanto mais mortos, mais clientes pra mim!", "Hehe, eu vendo até poções pros dois lados."],
    "guilda": ["Guildas... sempre precisam de mantimentos. E eu vendo tudo!"],
    "xingamento": ["Ei, cuidado com a língua, não aceito ofensas sem imposto!", "Pode me xingar, mas o preço vai dobrar."],
    "ferreiro": ["O ferreiro daqui é bom, mas cobra caro. Eu faria por menos... talvez."],
    "loja": ["Minha loja é modesta, mas honesta. Quer dizer... quase."],
    "taverna": ["Depois de beber, eles voltam pra comprar. Hahaha, adoro bêbados!"],
    "vilas": ["Rimvark é o coração do comércio! O resto? Só poeira e ratos."],
    "clima": ["Com sol ou chuva, o lucro sempre brilha pra mim."],
    "ajuda": ["Ajudar? Só se for pago adiantado."],
    "classes": ["Bruxos, cavaleiros... todos compram algo. No fim, somos iguais."],
    "economia": ["A economia? Eu sou a economia!"],
    "npcs": ["Ferreiro? Caríssimo. Eu? Justo... mais ou menos."],
    "elogios": ["Hehe, claro que é bom. Vem de Rimvark, afinal."],
    "pergunta estado": ["Estou ótimo! As vendas nunca dormem."],
    "despedida": ["Leve algo antes de ir. A porta é grátis, mas sair de mãos vazias não."],
}
respostas_comerciante_ebranthal = {
    "saudacao": ["Saudações, viajante. Está aqui para negociar?", "Bem-vindo a Ebrenthal, lar dos justos e dos ricos."],
    "batalha": ["Batalhas são inevitáveis... prepare-se bem, e talvez viva para comprar de novo."],
    "guilda": ["Guildas fortes movimentam o mercado. Aprecio isso."],
    "xingamento": ["Perdão, não falo a língua dos ignorantes."],
    "ferreiro": ["Nosso ferreiro é o melhor. Suas lâminas cortam até o silêncio."],
    "loja": ["Minha loja é simples, mas o valor está na qualidade, não no brilho."],
    "taverna": ["Taverna... um refúgio dos tolos e um abrigo dos cansados."],
    "vilas": ["Ebrenthal prospera enquanto o resto se perde na poeira."],
    "clima": ["Frio... perfeito para conservar tanto os corpos quanto os lucros."],
    "ajuda": ["Se busca ajuda, ofereça algo em troca. É assim que o mundo gira."],
    "classes": ["Toda classe tem seu preço. Alguns mais caros que outros."],
    "economia": ["A economia floresce onde há disciplina."],
    "npcs": ["Conheço todos. Vendo pra todos. Confio em ninguém."],
    "elogios": ["Agradeço. Excelência é o mínimo esperado em Ebrenthal."],
    "pergunta estado": ["Estou como sempre: produtivo."],
    "despedida": ["Volte quando seu bolso estiver mais pesado."],
}
respostas_comerciante_nocten = {
    "saudacao": ["Sombras e silêncio... bem-vindo a Nocten.", "Fala baixo... as paredes ouvem."],
    "batalha": ["A luta é apenas o eco da morte chamando cedo demais."],
    "guilda": ["Guildas? Correntes douradas com nomes diferentes."],
    "xingamento": ["As palavras ferem menos que a solidão. Escolha bem a sua."],
    "ferreiro": ["As lâminas daqui bebem o luar. São belas... e letais."],
    "loja": ["Nada aqui brilha, mas tudo tem poder."],
    "taverna": ["Bêbados cochicham segredos que valem mais que ouro."],
    "vilas": ["Nocten não dorme. Apenas espera."],
    "clima": ["O nevoeiro sussurra, o frio observa. É um bom dia."],
    "ajuda": ["Ajudar? Prefiro observar... mas talvez, por um preço."],
    "classes": ["Bruxos e cavaleiros... dois lados da mesma ruína."],
    "economia": ["Aqui, a economia é feita em segredos, não em moedas."],
    "npcs": ["Os rostos mudam, as intenções nunca."],
    "elogios": ["Heh... as sombras agradecem o elogio."],
    "pergunta estado": ["Estou... flutuando entre a paz e o abismo."],
    "despedida": ["Desapareça com cuidado. As sombras seguem quem brilha demais."],
}
respostas_barman = {
    "saudacao": ["Ora! Um rosto novo! Sente-se, a primeira dose é só metade do preço!"],
    "batalha": ["Batalha? Depois me conta tudo! Adoro um bom caos."],
    "guilda": ["Ah, guildas! Sempre vêm aqui beber depois de perder."],
    "xingamento": ["Ei! Sem brigar aqui dentro! O sangue mancha as mesas."],
    "ferreiro": ["O ferreiro? Grande amigo meu! Devemos metade da cerveja que ele bebe."],
    "loja": ["Loja? Aqui vendemos risadas e más decisões!"],
    "taverna": ["Minha taverna é o coração da vila. E o fígado também."],
    "vilas": ["Cada vila tem sua bebida... e seu bêbado favorito."],
    "clima": ["Se chover, bebemos dentro. Se fizer sol, bebemos fora!"],
    "ajuda": ["Ajuda? Tenho conselhos e cachaça. Qual prefere primeiro?"],
    "classes": ["Todo mundo vira herói depois de umas doses."],
    "economia": ["Economia? Aqui o dinheiro evapora em gargalhadas!"],
    "npcs": ["Conheço todos, mas lembro de poucos. Culpa da vodka."],
    "elogios": ["Hehe! Sabia que ia gostar da minha taverna!"],
    "pergunta estado": ["Feliz! Enquanto tiver copo cheio, tô vivo!"],
    "despedida": ["Volte logo, ou mando alguém te buscar no barril!"],
}
respostas_dorian = {
    "saudacao": ["opa...tudo bem?soube que você ainda tá tentando passar daquela arena infinita...eu te entendo... ", "vamos naquela arena?por que chega de ficar só aqui dentro desse abrigo"],
    "batalha": ["aceitaria estou bem forte e disposto ultimamente" ,"estou muito cansado...que tal batalhar depois?"],
    "guilda": [f"cara sou seu amigo claro que entraria na tua guilda,se a gente ficar mais forte podemos reeguer esse reino...", "se eu entrar na guilda por favo chama o {npc_aleatorio}"],
    "xingamento": ["hahahaha olha quem fala", "tu tá me xingando mas nunca se olhou no espelho não?"],
    "ferreiro": ["ele é um grande fornecedor de armas e equipamentos...só o preço que não acho muito bom", "o ferriero é gente boa, que tal a gente começar a arranjar materia prima pra ele,nos ganharia um mini salario e quem sabe um desconto?"],
    "vilas": ["calma...a vila é somente para negócios não para fazer viagem", "falando em vilas precisamos começar a comprar nossos equipamentos lá por que aqui em eldora ta cada vez mais caro"],
    "clima": ["se chover a gente se abriga na taverna ou na loja do ferreiro...", "tomara que chova ta ficando muito quente ultimamente"],
    "ajuda": ["ok......precisaria de ajuda em batalha,equipamentos,mineração ou exploração?", "cara qualquer coisa eu te ajudo financeiramente com as missões"],
    "classes": ["cara aproveita que um mago deu uma classe poderosa pra você por que eu não tenho nenhuma", "sua classe ajuda muito nas batalhas...aproveite isso"],
    "economia": ["ultimamente estou bem finaceiramente,faça as minhas missões que te dou uma parecla....", ""],
    "npcs": ["cara tá conversando muito para conhecer varias pessoas aqui", "eu não falo com nenhum....por que só acho eles estranho mesmo"],
    "elogios": ["obrigado,mas o foco é tentar sair desse lugar que não aguento mais!", "obrigado mas isso não me motiva mais!"],
    "pergunta estado": ["ah...tô bem pelo menos...", "to normal ultimamente"],
    "despedida": ["ok cara boa sorte!", "vá pela sombra......", "adeus...que deus guie sua mão"],                  
}
respostas_comerciante_eldora = {
    "saudacao": ["o quê!?????um freguês!!!como posso te ajudar olhe meu estoque como é variado!!!", "quê??um novo cidadão nesse reino destruido?o porque você veio aqui?"],
    "batalha": ["aceitaria estou bem forte e disposto ultimamente" ,"estou muito cansado...que tal batalhar depois?"],
    "guilda": [f"perai...você quer me chamar para sua guilda eu aceito!que me tire dessa loja entediante por favor!!", "ultimamenteestou mais focado no trabalho,volte depois se eu mudar de ideia"],
    "xingamento": ["quer ser expulso da minha loja??então me respeite também!", "pronto seu desconto não existe e acho melho renpensar suas ações"],
    "ferreiro": ["ele é um bom amigo,a gente vem falando sobre negócios em eldora"],
    "vilas":["faz muito tempo que eu não vou lá....você poderia me levar para reecontrar minha familia?", "ah Nocten onde eu nasci eu cresci que saudades mas nocten era uma vila muito escura e era melhor eu me mudar para eldora..."],
    "clima":["eu tenho minha loja como abrigo..como é bom dormir com aquele som de chuva", "quando fazer uma chuva não queiras fazer uma visita aqui para tomar um café?"],
    "ajuda": ["ok......precisaria de ajuda em batalha,equipamentos,mineração ou exploração?", "cara qualquer coisa eu te ajudo financeiramente com as missões"],
    "classes": ["cara aproveita que um mago deu uma classe poderosa pra você por que eu não tenho nenhuma", "sua classe ajuda muito nas batalhas...aproveite isso"],
    "economia": ["ultimamente estou bem finaceiramente,faça as minhas missões que te dou uma parecla....", ""],
    "npcs": ["cara tá conversando muito para conhecer varias pessoas aqui", "eu não falo com nenhum....por que só acho eles estranho mesmo"],
    "elogios": ["obrigado,mas o foco é tentar sair desse lugar que não aguento mais!", "obrigado mas isso não me motiva mais!"],
    "pergunta estado": ["ah...tô bem pelo menos...", "to normal ultimamente"],
    "despedida": ["ok cara boa sorte!", "vá pela sombra......", "adeus...que deus guie sua mão"],                  
}
respostas_npcs_procedurais = {
	"barman_procedural":resposta_procedural_barman,
}
resposta_npcs = {
    "barman":respostas_barman,
    "comerciante de rimvark":respostas_comerciante_rimvark,
    "comerciante de ebranthal":respostas_comerciante_ebranthal,
    "comerciante de nocten":respostas_comerciante_nocten,
    "comerciante de eldora":respostas_comerciante_eldora,
    "dorian":respostas_dorian,
    "comerciante sombrio":respostas_comerciante_sombrio,
    
    "comerciante de vangurd":respostas_comerciante_vangurd,
    
    "padre":respostas_padre,
    "dono do mercado rimvark":respostas_mercado_rimvark,
    "dono do mercado nocten":respostas_mercado_nocten,
    "dono do mercado ebranthal":respostas_mercado_ebranthal,
    "dono do mercado vangurd":respostas_mercado_vangurd,

}
puxar_assunto_barman = ["ora meu jovem,não aceitas uma bebida?aproveite que está metade do preço!", f"opa bem vindo de volta!o que deseja hoje?hoje eu tenho cerveja,uma cachaça das boa,uma vodka ou o classico velho barreiro?"]
memorias_curto_prazo = {
	"barman":[],
    "comerciante de rimvark":[],
    "comerciante de ebranthal":[],
    "comerciante de nocten":[],
    "comerciante de eldora":[],
    "dorian":[],
    "comerciante sombrio":[],
    "comerciante de vangurd":[],
    "padre":[],
    "dono do mercado rimvark":[],
    "dono do mercado nocten":[],
    "dono do mercado ebranthal":[],
    "dono do mercado vangurd":[],
}
emocoes_npcs = {
	"barman":None,
    "comerciante de rimvark":None,
    "comerciante de ebranthal":None,
    "comerciante de nocten":None,
    "comerciante de eldora":None,
    "dorian":None,
    "comerciante sombrio":None,
    "comerciante de vangurd":None,
    "padre":None,
    "dono do mercado rimvark":None,
    "dono do mercado nocten":None,
    "dono do mercado ebranthal":None,
    "dono do mercado vangurd":None,
}
dados_pergunta = {
	"sinais":[],
	"intenção":None,
	"tom":None,
}
def passer_memorias(pergunta):
	npc = npc_selecionado.lower()  # garante que pega o NPC certo
	for tema, lista_palavras in palavras_chaves.items():
		for palavra in lista_palavras:
			if palavra.lower() in pergunta.lower():
				memorias_curto_prazo[npc].append(tema)
def criar_emocao():
	pass
def identificar_estados(pergunta):
	if "?" in pergunta:
		dados_pergunta["sinais"].append("pergunta")
	if "!" in pergunta:
		dados_pergunta["sinais"].append("emoção")
	for palavra in palavras_chaves["xingamentos"]:
		if palavra in pergunta:
			dados_pergunta["sinais"].append("hostil")
	for palavra in palavras_chaves["elogio"]:
		if palavra["elogio"] in pergunta:
			dados_pergunta["sinais"].append("agrado")
	if len(pergunta.split()) >= 15:
		dados_pergunta["sinais"].append("desabafo")
	
	elif "pergunta" in dados_pergunta["sinais"] and "hostil" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "provocação"
	elif "pergunta" in dados_pergunta["sinais"] and "desabafo" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "ajuda"
	elif "pergunta" in dados_pergunta["sinais"] and "agrado" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "aprovação"
	elif "pergunta" in dados_pergunta["sinais"] and "hostil" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "raiva emocional"
	elif "agrado" in dados_pergunta["sinais"] and "hostil" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "manipular"
	elif "agrado" in dados_pergunta["sinais"] and "desabafo" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "confiar"
	elif "pergunta" in dados_pergunta["sinais"] and "desabafo" in dados_pergunta["sinais"] and "hostil" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "acusação"
	elif "pergunta" in dados_pergunta["sinais"] and "agrado" in dados_pergunta["sinais"] and "hostil" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "ironia"
	elif "pergunta" in dados_pergunta["sinais"] and "desabafo" in dados_pergunta["sinais"] and "agrado" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "pedido_sincero"
	elif "agrado" in dados_pergunta["sinais"] and "desabafo" in dados_pergunta["sinais"] and "hostil" in dados_pergunta["sinais"]:
		dados_pergunta["intenção"] = "instabilidade"
	else:
		dados_pergunta["intenção"] = "neutra"
def identificar_tom():
	pass
def npc_resposta_procedural(pergunta, npc_selecionado, respostas_npcs_procedurais):

    global resposta_npcs, palavras_chaves

    npc = npc_selecionado.lower()
    encontrou_tema = False
    pergunta_palavras = pergunta.split()
    contador_pergunta = 0
    dialogo = []

    for tema, lista_palavras in palavras_chaves.items():
        for palavra in pergunta_palavras:
            if palavra.lower() in lista_palavras:
                resposta_chat = respostas_npcs_procedurais[npc][tema]

                if callable(resposta_chat):
                    resposta_chat()
                else:
                    dialogo.append(random.choice(resposta_chat))

                contador_pergunta += 1
                encontrou_tema = True
                break  # achou o tema, sai do loop da lista de palavras

    for dialogo_final in dialogo:
        digitar(dialogo_final)

def melhorar_resposta():
    pass
#ações
#npc conversa com o player
def npc_resposta(pergunta,saida_dreamcore):
    global resposta_npcs, palavras_chaves
    encontrou_tema = False
    npc = npc_selecionado.lower()  # garante que pega o NPC certo
    for tema, lista_palavras in palavras_chaves.items():
        for palavra in lista_palavras:
            if palavra.lower() in pergunta.lower():  # compara pergunta com palavra-chave
                # pega a resposta correspondente ao tema do NPC
                resposta_chat = resposta_npcs[npc][tema]
                if callable(resposta_chat):
                    resposta_chat()
                else:
                    digitar(f"[{npc_selecionado}]: {random.choice(resposta_chat) if isinstance(resposta_chat, list) else resposta_chat}")

                encontrou_tema = True
                break  # saiu do loop das palavras
        if encontrou_tema:
            break  # saiu do loop dos temas
        
    if not encontrou_tema:
        resposta_indefinida = random.choice([
            "vai falar direito ou não?",
            "desculpa mas não entendi o que você falou",
            "acho que estou ficando surdo! poderia repetir?",
            "você gaguejando desse jeito! toma juízo rapaz"
            "poderia repetir?"
            "eu acho que essa palavra eu não conheço"
        ])
        digitar(f"[{npc_selecionado}]: {resposta_indefinida}")
        

                
npc_puxando_assunto = ""
def npc_puxar_assunto_jogador():
    if npc_puxando_assunto == "barman":
        
        dialogo_assunto_puxado = random.randint(0,1)
        digitar(puxar_assunto_barman[dialogo_assunto_puxado])

def humor():
    pass
def npc_resposta_npc(pergunta_npc_escolhida):
		pass
#menu da conversa#para quando tiverem dois npcs no mesmo lugar e os dois puxarem assunto
def npc_conversa_npc():
    
    
    assuntos = ["saudacao", "batalha", "guilda", "xingamento", "ferreiro", "vilas", "clima", "ajuda", "classes", "economia", "npcs", "elogios", "pergunta estado", "despedida"],
    tamanho_conversa = random.randint(4,25)
    linhas_escritas = 0
    conversa_entre_npc = []
    while linhas_escritas <= tamanho_conversa:
            
                
        assunto_escolhido = random.choice(assuntos)
        pergunta_npc_escolhida = random.choice(palavras_chaves[assunto_escolhido])
        conversa_entre_npc.append(pergunta_npc_escolhida)
        linhas_escritas +=1
        npc_resposta_npc(pergunta_npc_escolhida)
           
        linhas_escritas +=1
            
    
def iniciar_conversa():
    while True:
        global saida_dreamcore
        if not saida_dreamcore:
            break
        pergunta = input(">>[Dialogo]")
        if npc_selecionado.endswith("procedural"):
            npc_resposta_procedural(pergunta,npc_selecionado,respostas_npcs_procedurais)
        else:
            npc_resposta(pergunta,saida_dreamcore)
        if pergunta.lower() in ["sair", "adeus", "tchau", "fim", "fechar", "voltar"]:
            print("Você saiu da conversa.")
            break
if __name__ == "__main__":
	iniciar_conversa()
