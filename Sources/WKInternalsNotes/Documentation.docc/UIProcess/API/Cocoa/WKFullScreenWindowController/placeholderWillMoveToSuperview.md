# ``WKInternalsNotes/WKFullScreenWindowController/placeholderWillMoveToSuperview(_:)``

プレースホルダがビュー階層から外れる際のクリーンアップ判断を行う。

## Objective-C Declaration
```objective-c
- (void)placeholderWillMoveToSuperview:(UIView *)superview;
```

## Discussion
`PLATFORM(APPLETV)` 以外では、`superview` が `nil` になった場合にメインループへディスパッチし、プレースホルダが未配置かつ親が自身のままなら `close` を呼んでフルスクリーンを終了する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L1588`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1588)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
