// 页面加载后将光标聚焦到文本框
window.onload = function() {
    const editor = document.getElementById('content');
    editor.focus(); // 将焦点放到 contenteditable 的文本框
};

// 选择图片后显示文件名
document.getElementById('upload-button').addEventListener('click', function(event) {
    event.preventDefault(); // 阻止默认行为，防止按钮导致表单提交

    // 强制将光标设置在文本框内
    const editor = document.getElementById('content');
    editor.focus(); // 确保光标在文本框

    document.getElementById('image').click(); // 打开文件选择对话框
});

document.getElementById('image').addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        // 创建 FileReader 读取文件
        const reader = new FileReader();
        reader.onload = function(e) {
            // 获取编辑器区域
            const editor = document.getElementById('content');

            // 在光标位置插入图片
            const img = document.createElement('img');
            img.src = e.target.result;
            img.alt = file.name;
            img.style.maxWidth = '100%';

            // 将图片插入到编辑器的当前位置
            const range = window.getSelection().getRangeAt(0);
            range.insertNode(img);
        };
        reader.readAsDataURL(file);

        // 清空文件输入框的值，允许同一张图片多次上传
        document.getElementById('image').value = '';
    }
});
