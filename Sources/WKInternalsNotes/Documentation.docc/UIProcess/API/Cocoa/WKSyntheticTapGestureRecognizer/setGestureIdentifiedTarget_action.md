# ``WKInternalsNotes/WKSyntheticTapGestureRecognizer/setGestureIdentifiedTarget(_:action:)``

認識時に呼び出す target/action を設定する。

## Objective-C Declaration
```objective-c
- (void)setGestureIdentifiedTarget:(id)target action:(SEL)action;
```

## Discussion
`_gestureIdentifiedTarget` と `_gestureIdentifiedAction` に保存し、`setState:` が `Ended` のときに呼ばれる。

## References
- [`WKSyntheticTapGestureRecognizer.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.h#L37)
- [`WKSyntheticTapGestureRecognizer.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
