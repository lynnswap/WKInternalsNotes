# ``WKInternalsNotes/WKInspectorNodeSearchGestureRecognizer/locationInView(_:)``

保持しているタッチの位置を返す。

## Objective-C Declaration
```objective-c
- (CGPoint)locationInView:(UIView *)view;
```

## Discussion
内部で保持している `UITouch` の `locationInView:` を呼び出して座標を返す。

## References
- [`WKInspectorNodeSearchGestureRecognizer.mm#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/ios/WKInspectorNodeSearchGestureRecognizer.mm#L37)
- [`WKInspectorNodeSearchGestureRecognizer.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/ios/WKInspectorNodeSearchGestureRecognizer.h#L31)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
