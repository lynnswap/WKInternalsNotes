# ``WKInternalsNotes/WKDeferringGestureRecognizer/endDeferral(_:)``

デファラの遅延状態を終了する。

## Objective-C Declaration
```objective-c
- (void)endDeferral:(WebKit::ShouldPreventGestures)shouldPreventGestures;
```

## Discussion
`ShouldPreventGestures::Yes` の場合は `state` を `Ended`、それ以外は `Failed` に設定する。

## References
- [`WKDeferringGestureRecognizer.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.h#L51)
- [`WKDeferringGestureRecognizer.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.mm#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
