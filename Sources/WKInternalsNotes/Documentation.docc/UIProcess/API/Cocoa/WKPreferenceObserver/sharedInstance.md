# ``WKInternalsNotes/WKPreferenceObserver/sharedInstance()``

共有インスタンスを返す。

## Objective-C Declaration
```objective-c
+ (id)sharedInstance;
```

## Discussion
`NeverDestroyed` で保持した `WKPreferenceObserver` を生成・返却するシングルトン実装。

## References
- [`PreferenceObserver.h#L28`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/PreferenceObserver.h#L28)
- [`PreferenceObserver.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/PreferenceObserver.mm#L123)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
