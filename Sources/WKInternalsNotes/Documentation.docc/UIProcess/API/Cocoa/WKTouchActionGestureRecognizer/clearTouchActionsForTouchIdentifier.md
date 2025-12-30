# ``WKInternalsNotes/WKTouchActionGestureRecognizer/clearTouchActionsForTouchIdentifier(_:)``

タッチ識別子の設定を削除する。

## Objective-C Declaration
```objective-c
- (void)clearTouchActionsForTouchIdentifier:(unsigned)touchIdentifier;
```

## Discussion
`_touchActionsByTouchIdentifier` から該当エントリを削除する。

## References
- [`WKTouchActionGestureRecognizer.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.h#L37)
- [`WKTouchActionGestureRecognizer.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchActionGestureRecognizer.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
