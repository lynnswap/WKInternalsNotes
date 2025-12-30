# ``WKInternalsNotes/WKTouchActionGestureRecognizer/setTouchActions(_:forTouchIdentifier:)``

タッチ識別子に対応する `touch-action` を設定する。

## Objective-C Declaration
```objective-c
- (void)setTouchActions:(OptionSet<WebCore::TouchAction>)touchActions forTouchIdentifier:(unsigned)touchIdentifier;
```

## Discussion
`TouchAction::Auto` を含まないことを確認し、`_touchActionsByTouchIdentifier` に保存する。

## References
- [`WKTouchActionGestureRecognizer.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.h#L36)
- [`WKTouchActionGestureRecognizer.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
