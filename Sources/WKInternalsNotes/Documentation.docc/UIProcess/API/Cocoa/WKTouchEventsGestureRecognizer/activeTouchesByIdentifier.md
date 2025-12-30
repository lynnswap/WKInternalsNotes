# ``WKInternalsNotes/WKTouchEventsGestureRecognizer/activeTouchesByIdentifier``

タッチ識別子から `UITouch` を引けるマップを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSMapTable<NSNumber *, UITouch *> *activeTouchesByIdentifier;
```

## Default Value
`initWithContentView:` で `NSMapTable.strongToWeakObjectsMapTable` を作成する。

## Discussion
getter は `_activeTouchesByIdentifier` を返す。`_recordTouches` で内容を入れ替える。

## References
- [`WKTouchEventsGestureRecognizer.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.h#L76)
- [`WKTouchEventsGestureRecognizer.mm#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L83)
- [`WKTouchEventsGestureRecognizer.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L91)
- [`WKTouchEventsGestureRecognizer.mm#L304`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L304)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
