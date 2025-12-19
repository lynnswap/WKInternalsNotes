# ``WKInternalsNotes/WKProcessPool/_pluginLoadClientPolicies``

プラグイン読み込みクライアントポリシーを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSDictionary *_pluginLoadClientPolicies WK_API_AVAILABLE(macos(10.13));
```

## Default Value
`@{ }`（空の辞書）。

## Discussion
実装は空の `NSDictionary` を返すのみで、状態は保持しない。

## References
- [`WKProcessPoolPrivate.h#L96`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L96)
- [`WKProcessPool.mm#L309`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L309)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
