# ``WKInternalsNotes/WKFileUploadPanel/repositionContextMenuIfNeeded(_:)``

必要に応じてコンテキストメニューの位置を調整する。

## Objective-C Declaration
```objective-c
- (void)repositionContextMenuIfNeeded:(WebKit::KeyboardIsDismissing)isKeyboardBeingDismissed;
```

## Discussion
キーボードの表示状態や入力ビューの位置を確認し、表示位置が覆われる場合にメニューを再表示する。

## References
- [`WKFileUploadPanel.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.h#L59)
- [`WKFileUploadPanel.mm#L810`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.mm#L810)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
