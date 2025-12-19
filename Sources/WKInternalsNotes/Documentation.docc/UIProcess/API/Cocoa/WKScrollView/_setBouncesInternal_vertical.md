# ``WKInternalsNotes/WKScrollView/_setBouncesInternal(_:vertical:)``

内部側のバウンス可否を設定する。

## Objective-C Declaration
```objective-c
- (void)_setBouncesInternal:(BOOL)horizontal vertical:(BOOL)vertical;
```

## Discussion
内部の水平/垂直バウンスフラグを更新し、クライアント設定との AND で `bouncesHorizontally`/`bouncesVertically` を更新する。

## References
- [`WKScrollView.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L43)
- [`WKScrollView.mm#L479`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L479)
- [`WKScrollView.mm#L486`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L486)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
