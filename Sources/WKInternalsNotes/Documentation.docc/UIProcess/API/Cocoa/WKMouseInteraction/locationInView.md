# ``WKInternalsNotes/WKMouseInteraction/locationInView(_:)``

現在のマウス/ホバー位置を指定ビュー座標で返す。

## Objective-C Declaration
```objective-c
- (CGPoint)locationInView:(UIView *)view;
```

## Discussion
`mouseTouch` が存在し、かつキャンセル/退出状態でなければ `locationInView:` を返す。そうでなければ `(-1, -1)` を返す。

## References
- [`WKMouseInteraction.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L46)
- [`WKMouseInteraction.mm#L430`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L430)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
