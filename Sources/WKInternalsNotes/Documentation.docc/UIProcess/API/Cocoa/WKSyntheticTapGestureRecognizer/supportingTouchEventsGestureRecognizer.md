# ``WKInternalsNotes/WKSyntheticTapGestureRecognizer/supportingTouchEventsGestureRecognizer``

補助となる `WKTouchEventsGestureRecognizer` を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) WKTouchEventsGestureRecognizer *supportingTouchEventsGestureRecognizer;
```

## Default Value
自動合成されるため初期値は `nil`。

## Discussion
`touchesEnded` で `activeTouchesByIdentifier` を参照するために使用される。

## References
- [`WKSyntheticTapGestureRecognizer.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.h#L40)
- [`WKSyntheticTapGestureRecognizer.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.mm#L81)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
