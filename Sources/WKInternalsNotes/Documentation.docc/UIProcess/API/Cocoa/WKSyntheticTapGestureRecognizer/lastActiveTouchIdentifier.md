# ``WKInternalsNotes/WKSyntheticTapGestureRecognizer/lastActiveTouchIdentifier``

最後にアクティブだったタッチ識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSNumber *lastActiveTouchIdentifier;
```

## Default Value
`touchesEnded` で更新され、`reset` で `nil` に戻る。

## Discussion
`_lastActiveTouchIdentifier` を返す。

## References
- [`WKSyntheticTapGestureRecognizer.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.h#L41)
- [`WKSyntheticTapGestureRecognizer.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKSyntheticTapGestureRecognizer.mm#L97)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
