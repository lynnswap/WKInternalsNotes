# ``WKInternalsNotes/WKProcessPool/_coreLocationProvider``

Core Location の provider を取得・設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCoreLocationProvider:) id <_WKGeolocationCoreLocationProvider> _coreLocationProvider WK_API_AVAILABLE(ios(11.0));
```

## Default Value
未設定の場合は `nil`。

## Discussion
getter は `_coreLocationProvider` を返す。setter は `_geolocationProvider` が作成済みの場合に例外を投げ、それ以外は `_coreLocationProvider` を更新する。

## References
- [`WKProcessPoolPrivate.h#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L103)
- [`WKProcessPool.mm#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L103)
- [`WKProcessPool.mm#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L103)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
