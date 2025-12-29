# ``WKInternalsNotes/WKMouseInteraction/lastLocation``

最後に記録した位置を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) std::optional<CGPoint> lastLocation;
```

## Default Value
ホバーやマウスタッチ更新時に記録される。未記録時は空。

## Discussion
`_hoverGestureRecognized:` と `_updateMouseTouches:` で `_lastLocation` を更新する。

## References
- [`WKMouseInteraction.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L57)
- [`WKMouseInteraction.mm#L378`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L378)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
