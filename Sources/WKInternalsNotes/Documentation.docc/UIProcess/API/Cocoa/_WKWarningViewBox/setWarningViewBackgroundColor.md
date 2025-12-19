# ``WKInternalsNotes/_WKWarningViewBox/setWarningViewBackgroundColor(_:)``

警告ビューの背景色を設定する。

## Objective-C Declaration
```objective-c
- (void)setWarningViewBackgroundColor:(WebCore::CocoaColor *)color;
```

## Discussion
macOS では `_backgroundColor` を保持して `wantsLayer` を有効化し、iOS では `backgroundColor` を直接設定する。

## References
- [`_WKWarningView.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/_WKWarningView.h#L60)
- [`_WKWarningView.mm#L286`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/_WKWarningView.mm#L286)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
