# ``WKInternalsNotes/_WKJSHandle/world``

関連する `WKContentWorld` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, weak) WKContentWorld *world;
```

## Default Value
`_ref->info().worldIdentifier` に対応する `WKContentWorld`。

## Discussion
`ContentWorld::worldForIdentifier` の結果を返す。

## References
- [`_WKJSHandle.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKJSHandle.h#L40)
- [`_WKJSHandle.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKJSHandle.mm#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
