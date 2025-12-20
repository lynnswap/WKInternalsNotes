# ``WKInternalsNotes/WKColorExtensionView/initWithFrame(_:delegate:)``

カラー拡張ビューを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(CGRect)frame delegate:(id<WKColorExtensionViewDelegate>)delegate;
```

## Discussion
`CocoaView` を `frame` で初期化し、`delegate` を保持して `hidden = YES` に設定する。

## References
- [`WKColorExtensionView.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.h#L46)
- [`WKColorExtensionView.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L43)
- [`WKColorExtensionView.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L48)
- [`WKColorExtensionView.mm#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
