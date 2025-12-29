# ``WKInternalsNotes/_WKTargetedElementInfo/nearbyTarget``

近傍ターゲットかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isNearbyTarget) BOOL nearbyTarget;
```

## Default Value
`API::TargetedElementInfo::isNearbyTarget()` の値。

## Discussion
内部の `_info` から `isNearbyTarget()` を取得して返す。

## References
- [`_WKTargetedElementInfo.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.h#L46)
- [`_WKTargetedElementInfo.mm#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementInfo.mm#L152)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
