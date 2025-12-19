# ``WKInternalsNotes/WKContentView/textInputTraitsForWebView``

WebView 向けの `UITextInputTraits` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UITextInputTraits *textInputTraitsForWebView;
```

## Default Value
未生成なら `UITextInputTraits` を生成し、必要なら更新して返す。

## Discussion
`_legacyTextInputTraits` が未生成の場合に `UITextInputTraits` を生成する。フォーカスを外す処理中でない場合は `_updateTextInputTraits:` を呼んで内容を更新し、そのインスタンスを返す。

## References
- [`WKContentViewInteraction.h#L731`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L731)
- [`WKContentViewInteraction.mm#L7209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7209)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
