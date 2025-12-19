# ``WKInternalsNotes/WKContentView/updateSoftwareKeyboardSuppressionStateFromWebView()``

WebView 側のソフトキーボード抑制状態を反映する。

## Objective-C Declaration
```objective-c
- (void)updateSoftwareKeyboardSuppressionStateFromWebView;
```

## Discussion
WebView が抑制中ならその状態に合わせ、解除待ちの場合は自動補正コンテキストの更新を要求する。

## References
- [`WKContentViewInteraction.h#L951`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L951)
- [`WKContentViewInteraction.mm#L6095`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6095)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
