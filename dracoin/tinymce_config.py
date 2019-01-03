import os
from urllib.parse import urljoin


# TinyMCE configuration
TINYMCE_POST_CONFIG = {
    'selector': 'textarea',
    # 'language': 'en-GB',
    # 'language_url': urljoin(STATIC_URL, 'languages/en_GB.js'),
    # 'language': 'uk',
    # 'language_url': urljoin(STATIC_URL, 'languages/uk.js'),
    # 'language_url': '../../../../static/languages/uk.js',
    # 'language_url': os.path.join(BASE_DIR, 'static/languages/uk.js'),
    # 'language': 'ru',
    # 'language_url': urljoin(STATIC_URL, 'languages/ru.js'),
    'content_css': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css',
    'width': 'auto',
    'height': 360,
    'plugins': [
      'autosave advlist autolink link image lists charmap print preview hr anchor pagebreak \
      searchreplace wordcount visualblocks visualchars code fullscreen \
      insertdatetime media nonbreaking save table contextmenu directionality emoticons \
      paste codesample help',
    ],
    'inline': False,
    'contextmenu': 'link anchor image',
    'menubar': 'file edit insert view format table help',
    'statusbar': True,
    'toolbar1': 'alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | searchreplace visualblocks fullscreen preview code',
    'toolbar2': 'bold italic underline | link anchor image blockquote charmap hr codesample',
    'codesample_languages': [
        {'text': 'C-like', 'value': 'clike'},
        {'text': 'C++', 'value': 'cpp'},
        {'text': 'Makefile', 'value': 'makefile'},
        {'text': 'Python', 'value': 'python'},
        {'text': 'Django/Jinja2', 'value': 'django'},
        {'text': 'Haskell', 'value': 'haskell'},
        {'text': 'SQL', 'value': 'sql'},
        {'text': 'JSON+JSONP', 'value': 'json'},
        {'text': 'HTML/XML', 'value': 'html'},
        {'text': 'CSS', 'value': 'css'},
        {'text': 'JavaScript', 'value': 'javascript'},
        {'text': 'Diff', 'value': 'diff'},
        {'text': 'Docker', 'value': 'docker'},
        {'text': 'Git', 'value': 'git'},
        {'text': 'Markdown', 'value': 'markdown'},
        {'text': 'LaTeX', 'value': 'latex'},
        {'text': 'Arduino', 'value': 'arduino'},
    ],
}


TINYMCE_COMMENT_CONFIG = {
    'selector': 'textarea',
    'content_css': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css',
    'width': 'auto',
    'height': 200,
    'plugins': [
      'autosave advlist autolink link lists charmap preview wordcount insertdatetime emoticons paste codesample',
    ],
    'inline': False,
    'contextmenu': False,
    'menubar': False,
    'statusbar': True,
    'toolbar1': 'undo redo | bold italic underline | charmap codesample link blockquote emoticons | preview',
    'codesample_languages': [
        {'text': 'C-like', 'value': 'clike'},
        {'text': 'C++', 'value': 'cpp'},
        {'text': 'Makefile', 'value': 'makefile'},
        {'text': 'Python', 'value': 'python'},
        {'text': 'Django/Jinja2', 'value': 'django'},
        {'text': 'Haskell', 'value': 'haskell'},
        {'text': 'SQL', 'value': 'sql'},
        {'text': 'JSON+JSONP', 'value': 'json'},
        {'text': 'HTML/XML', 'value': 'html'},
        {'text': 'CSS', 'value': 'css'},
        {'text': 'JavaScript', 'value': 'javascript'},
        {'text': 'Diff', 'value': 'diff'},
        {'text': 'Docker', 'value': 'docker'},
        {'text': 'Git', 'value': 'git'},
        {'text': 'Markdown', 'value': 'markdown'},
        {'text': 'LaTeX', 'value': 'latex'},
        {'text': 'Arduino', 'value': 'arduino'},
    ]
}
