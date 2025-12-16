# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_textInteractionGesturesEnabled``

text selection / interaction gestures を有効/無効にする（iOS）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setTextInteractionGesturesEnabled:) BOOL _textInteractionGesturesEnabled WK_API_DEPRECATED_WITH_REPLACEMENT("WKPreferences.textInteractionGesturesEnabled", ios(12.0, 15.0));
```

## Default Value
iOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_textInteractionGesturesEnabled = YES`: text interaction gestures（テキスト選択/操作）を有効にする（ただし `page->preferences().textInteractionEnabled()` も必要）。
- `_textInteractionGesturesEnabled = NO`: `WKContentViewInteraction` が early return し、テキスト選択/操作の判定や UI（例: selection tint）の更新が行われなくなる。

## Details
- `WKPrivateDeprecated`（iOS 12–15）
- 置換先として `WKPreferences.textInteractionGesturesEnabled` が指定されているが、公開ヘッダ（`WKPreferences.h` 等）では確認できない

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L191)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L256`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L256)
- [`Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3630`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3630)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
