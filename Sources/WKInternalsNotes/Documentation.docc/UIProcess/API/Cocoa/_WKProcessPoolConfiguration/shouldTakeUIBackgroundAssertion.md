# ``WKInternalsNotes/_WKProcessPoolConfiguration/shouldTakeUIBackgroundAssertion``

iOS で UIProcess がバックグラウンドアサーションを取得するかを制御する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldTakeUIBackgroundAssertion WK_API_AVAILABLE(ios(11.0));
```

## Default Value
既定値は `true`。

## Discussion
`PLATFORM(IOS_FAMILY)` でのみ利用され、getter/setter は `ProcessPoolConfiguration` の `shouldTakeUIBackgroundAssertion` を直接操作する。

## References
- [`_WKProcessPoolConfiguration.mm#L327`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L327)
- [`_WKProcessPoolConfiguration.mm#L332`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L332)
- [`APIProcessPoolConfiguration.h#L185`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L185)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
