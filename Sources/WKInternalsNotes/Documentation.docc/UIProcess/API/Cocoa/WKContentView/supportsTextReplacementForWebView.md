# ``WKInternalsNotes/WKContentView/supportsTextReplacementForWebView``

テキスト置換が可能かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL supportsTextReplacementForWebView;
```

## Default Value
`self.webView._editable` を返す。

## Discussion
`WKWebView` の編集可能状態をそのまま返す getter。

## References
- [`WKContentViewInteraction.h#L985`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L985)
- [`WKContentViewInteraction.mm#L12764`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12764)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
