# ``WKInternalsNotes/WKProcessPool/_geolocationProvider``

プロセスプール用の `WKGeolocationProviderIOS` を返す。

## Objective-C Declaration
```objective-c
@property(readonly) WKGeolocationProviderIOS *_geolocationProvider;
```

## Default Value
初回アクセス時に `[[WKGeolocationProviderIOS alloc] initWithProcessPool:*_processPool]` で生成したもの。

## Discussion
`_geolocationProvider` が未生成なら作成して保持し、以降はキャッシュされたインスタンスを返す。

## References
- [`WKProcessPoolInternal.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolInternal.h#L51)
- [`WKProcessPool.mm#L182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L182)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
