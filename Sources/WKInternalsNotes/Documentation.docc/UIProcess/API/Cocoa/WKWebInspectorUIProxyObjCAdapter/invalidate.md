# ``WKInternalsNotes/WKWebInspectorUIProxyObjCAdapter/invalidate()``

UIProxy との参照を無効化する。

## Objective-C Declaration
```objective-c
- (void)invalidate;
```

## Discussion
保持している `WebInspectorUIProxy` の弱参照を `nullptr` にして切り離す。

## References
- [`WKInspectorPrivateMac.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/mac/WKInspectorPrivateMac.h#L43)
- [`WebInspectorUIProxyMac.mm#L112`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L112)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
