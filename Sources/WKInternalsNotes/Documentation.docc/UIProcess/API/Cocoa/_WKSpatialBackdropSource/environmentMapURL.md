# ``WKInternalsNotes/_WKSpatialBackdropSource/environmentMapURL``

環境マップの URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSURL *environmentMapURL WK_API_AVAILABLE(visionos(26.0));
```

## Default Value
`SpatialBackdropSource` に `environmentMapURL` がある場合に設定される。

## Discussion
`SpatialBackdropSource` の `m_environmentMapURL` があれば `NSURL` に変換して保持する。

## References
- [`_WKSpatialBackdropSource.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSpatialBackdropSource.h#L36)
- [`_WKSpatialBackdropSource.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSpatialBackdropSource.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
