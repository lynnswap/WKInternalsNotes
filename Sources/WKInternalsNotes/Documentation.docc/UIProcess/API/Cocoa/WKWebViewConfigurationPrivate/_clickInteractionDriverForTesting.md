# ``WKInternalsNotes/WKWebViewConfiguration/_clickInteractionDriverForTesting``

click interaction driver（テスト用）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setClickInteractionDriverForTesting:) id <_UIClickInteractionDriving> _clickInteractionDriverForTesting WK_API_AVAILABLE(ios(13.0));
```

## Default Value
iOS: `nil`

## Discussion
- この API を使わない場合: click interaction は通常のドライバで処理される（`nil`）。
- `_clickInteractionDriverForTesting` を設定すると: context menu の presentation が使う driver を override できる（テスト用）。
- `nil` に戻すと: override を解除する。

## Details
- テスト用

## References
- [`WKWebViewConfigurationPrivate.h#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L123)
- [`WKWebViewConfiguration.mm#L946`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L946)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
