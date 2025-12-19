# ``WKInternalsNotes/WKContentView/_setTextColorForWebView(_:sender:)``

テキスト色を変更する。

## Objective-C Declaration
```objective-c
- (void)_setTextColorForWebView:(UIColor *)color sender:(id)sender;
```

## Discussion
UIColor を `WebCore::Color` に変換して `ForeColor` コマンドを実行する。

## References
- [`WKContentViewInteraction.h#L787`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L787)
- [`WKContentViewInteraction.mm#L4555`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4555)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
