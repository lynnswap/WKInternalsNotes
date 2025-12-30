# ``WKInternalsNotes/_WKSpatialBackdropSource/modelURL``

モデルの URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *modelURL WK_API_AVAILABLE(visionos(26.0));
```

## Default Value
`initWithSpatialBackdropSource:` で `SpatialBackdropSource` の URL をコピーして設定される。

## Discussion
`SpatialBackdropSource` の `m_modelURL` を `NSURL` に変換して保持する。

## References
- [`_WKSpatialBackdropSource.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSpatialBackdropSource.h#L35)
- [`_WKSpatialBackdropSource.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSpatialBackdropSource.mm#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
