# ``WKInternalsNotes/WKView/_doAfterNextPresentationUpdate(_:)``

次のプレゼンテーション更新後にブロックを実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterNextPresentationUpdate:(void (^)(void))updateBlock WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
WKView では空実装で、block は実行されない。

## References
- [`WKViewPrivate.h#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L142)
- [`WKView.mm#L1378`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1378)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
