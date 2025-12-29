# ``WKInternalsNotes/_WKInspectorConfiguration/processPool``

インスペクターが使用する `WKProcessPool`。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, nullable) WKProcessPool *processPool;
```

## Default Value
`nil`。

## Discussion
setter で `API::InspectorConfiguration` に `processPool` を設定し、getter は内部の `WebProcessPool` を `WKProcessPool` にラップして返す。

## References
- [`_WKInspectorConfiguration.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorConfiguration.h#L54)
- [`_WKInspectorConfiguration.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorConfiguration.mm#L72)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
