async function carregarPerfil() {
    const resposta = await fetch("http://127.0.0.1:8000/perfil");
    const dados = await resposta.json();


    const dadosPessoais = document.getElementById("dados-pessoais");
    dadosPessoais.innerHTML = `
        <p><strong>Nome:</strong> ${dados.nome}</p>
        <p><strong>Idade:</strong> ${dados.idade} anos</p>
        <p><strong>Formação Acadêmica:</strong> ${dados.formacao.join(", ")}</p>
        <p><strong>Email:</strong> ${dados.email}</p>
        <p><strong>Celular:</strong> ${dados.celular}</p>
    `;


    const experiencias = document.getElementById("experiencias");
    dados.experiencias.forEach(exp => {
        experiencias.innerHTML += `
            <p><strong>${exp.titulo}</strong> — ${exp.empresa} (${exp.periodo})<br>
            ${exp.descricao}</p>
        `;
    });


    const projetos = document.getElementById("projetos");
    dados.projetos.forEach(proj => {
        projetos.innerHTML += `
            <p><strong>${proj.titulo}</strong><br>
            ${proj.descricao}</p>
        `;
    });


    const habilidades = document.getElementById("habilidades");
    dados.habilidades.forEach(h => {
        habilidades.innerHTML += `
            <p>${h.nome}</p>
            <div class="barra"><div class="progresso" data-nivel="${h.nivel}"></div></div>
        `;
    });


    setTimeout(() => {
        document.querySelectorAll(".progresso").forEach(barra => {
            const nivel = barra.getAttribute("data-nivel");
            barra.style.width = nivel + "%";
        });
    }, 100);
}

carregarPerfil();