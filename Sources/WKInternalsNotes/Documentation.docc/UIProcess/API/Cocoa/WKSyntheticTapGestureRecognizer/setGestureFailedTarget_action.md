# ``WKInternalsNotes/WKSyntheticTapGestureRecognizer/setGestureFailedTarget(_:action:)``

失敗時に呼び出す target/action を設定する。

## Objective-C Declaration
```objective-c
- (void)setGestureFailedTarget:(id)target action:(SEL)action;
```

## Discussion
`_gestureFailedTarget` と `_gestureFailedAction` に保存し、`setState:` が `Failed` のときに呼ばれる。

## References
- [`WKSyntheticTapGestureRecognizer.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.h#L38)
- [`WKSyntheticTapGestureRecognizer.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
