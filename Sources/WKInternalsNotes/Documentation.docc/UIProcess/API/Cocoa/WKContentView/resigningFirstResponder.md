# ``WKInternalsNotes/WKContentView/resigningFirstResponder``

ファーストレスポンダーを辞める処理中かを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isResigningFirstResponder) BOOL resigningFirstResponder;
```

## Default Value
`_resigningFirstResponder` を返す。

## Discussion
`resignFirstResponderForWebView` の実行中に `SetForScope` で `YES` になり、処理終了後に戻る内部フラグ。

## References
- [`WKContentView.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L63)
- [`WKContentViewInteraction.h#L576`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L576)
- [`WKContentViewInteraction.mm#L2126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2126)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
